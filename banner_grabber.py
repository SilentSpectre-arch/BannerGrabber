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

def grab_banner(target,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((target,port))

        print(f'[+] {target}:{port} open')

        banner= sock.recv(1024)

        if banner:
            banner = banner.decode(errors='ignore').strip()
            print(f"    Banner:{banner}")
        else:
            print("No banner received")

    except socket.timeout:
        print(f'[-] TimeOut')

    except ConnectionRefusedError:
        print(f'[-] {target}:{port} CLOSED')

    except Exception as e:
        print(f'[-] {target}:{port} ERROR: {e}')

    finally:
        sock.close()

def grab_http_banner(target,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((target,port))

        request = (
            f'HEAD / HTTP/1.1\r\n'
            f'Host: {target}\r\n'
            f'Connection: close\r\n'
            f'\r\n'
        )

        sock.sendall(request.encode())

        response=sock.recv(4096)

        print(f'[+] {target}:{port} HTTP OPEN')
        print(response.decode(errors='ignore'))

    except socket.timeout:
        print(f"[-] {target}:{port} TIMEOUT")

    except ConnectionRefusedError:
        print(f'[-] {target}:{port} CLOSED')

    except Exception as e:
        print(f'[-] {target}:{port} ERROR: {e}')

    finally:
        sock.close()

target = input("Enter target: ")

ports = [21,22,23,25,53,80,110,143,443,3306,8080]

for port in ports:
    grab_banner(target,port)

