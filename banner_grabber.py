#!/usr/bin/env python3

import socket

target=input("Enter target: ")

port=int(input("Enter port: "))

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(3)

result=sock.connect_ex((target, port))

if result == 0:
    print(f"[+] {target}:{port} is open")
else:
    print(f'[-] {target}:{port} is closed')

sock.close()