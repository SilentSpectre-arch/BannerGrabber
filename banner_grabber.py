#!/usr/bin/env python3

import socket
import re

# Probes table
HTTP_PORTS={80,8000,8080}

def extract_server_header(response):
    match=re.search(r"^Server:\s*(.+)$", response,
                    re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def identify_service(port,banner):
    if port in HTTP_PORTS:
        return "HTTP", banner

    if banner.startswith("SSH-"):
        version= banner.split("-")[2].split()[0]
        return "SSH",version

    if "FTP" in banner.upper():
        return "FTP",banner

    if "SMTP" in banner.upper():
        return "SMTP",banner

    if banner:
        return "Unkown",banner
    return "Unkown","-"

def grab_banner(target,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((target,port))
        if port in HTTP_PORTS:
            request=(
                f'HEAD / HTTP/1.1\r\n'
                f'Host: {target}\r\n'
                f'Connection: close\r\n'
                f'\r\n'
            )
            sock.sendall(request.encode())
            data=sock.recv(4096).decode(errors="ignore")

            server=extract_server_header(data)
            service, version=identify_service(port, server if server else"")

            print(f'{port}/tcp\tOPEN\t{service}\t{version}')
        else:
            banner=sock.recv(1024).decode(errors="ignore").strip()
            service,version=identify_service(port,banner)

            print(f'{port}/tcp\tOPEN\t{service}\t{version}')
    except socket.timeout:
        print(f'{port}/tcp\tTIMEOUT\t-\t-')

    except ConnectionRefusedError:
        print(f'{port}/tcp\tCLOSED\t-\t-')

    except Exception as e:
        print(f'{port}/tcp\tERROR\t-\t{e}')

    finally:
        sock.close()
        
target = input("Enter target: ")

ports = [21,22,23,25,53,80,110,143,443,3306,8080,8000]

for port in ports:
    grab_banner(target,port)

