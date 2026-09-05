# Banner Grabber

A simple Python-based Banner Grabber that scans common TCP ports, identifies open services, and extracts version information from service banners.

This project demonstrates basic socket programming, service fingerprinting, and HTTP header parsing using Python.

## Features

- Scan common TCP ports
- Detect open, closed, timeout, and error states
- Identify common services:
  - HTTP
  - SSH
  - FTP
  - SMTP
- Extract the **Server** header from HTTP responses
- Display service version information when available
- Built using Python's standard library only

## Supported Ports

The scanner checks the following ports by default:

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 8000 | HTTP |
| 8080 | HTTP |

## Requirements

- Python 3.x
- No external dependencies

## Usage

```bash
git clone https://github.com/SilentSpectre-arch/BannerGrabber.git
```

```bash
python3 banner_grabber.py
```

Enter a target IP address or hostname:

```text
Enter target: 127.0.0.1
```

## Example Output

```text
Enter target: scanme.nmap.org

21/tcp   CLOSED   -      -
22/tcp   OPEN     SSH    OpenSSH_6.6.1
25/tcp   CLOSED   -      -
80/tcp   OPEN     HTTP   Apache/2.4.7
443/tcp  OPEN     HTTP   nginx/1.18.0
8080/tcp CLOSED   -      -
```

## How It Works

The scanner uses Python sockets to establish TCP connections.

- **HTTP ports (80, 8000, 8080):**
  - Sends a `HEAD` request.
  - Extracts the `Server` header using regular expressions.
- **Other ports:**
  - Reads the service banner immediately after connecting.
  - Matches common banner patterns to identify the service and version.

## Learning Objectives

This project helps practice:

- Python socket programming
- TCP communication
- Banner grabbing
- HTTP protocol basics
- Regular expressions (`re`)
- Basic service fingerprinting

## Limitations

- Scans only a predefined list of ports.
- HTTPS (443) is treated as a TCP connection and does not perform a TLS handshake.
- Some services do not send banners automatically.
- This is intended as a learning project, not a replacement for tools like Nmap.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not scan systems without permission.