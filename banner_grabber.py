#!/usr/bin/env python3

import socket

target=input("Enter target: ")

port=int(input("Enter port: "))

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(3)

try:

    result=sock.connect((target,port))

    print(f'[+] Connected to {target}:{port}')

    banner=sock.recv(1024)

    print(f'[+] Banner: {banner.decode(errors='ignore').strip()}')

except socket.timeout:
    print("[-] Connection timed out")

except ConnectionRefusedError:
    print(f"[-] Connection refused")

except Exception as e:
    print(f'[-] Error: {e}')

finally:
    sock.close()