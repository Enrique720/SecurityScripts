# SecurityScripts

A curated collection of scripts, command references, and resources for penetration testing, network reconnaissance, and general security assessments.

## Contents

- **nmap/nmap_commands.md**  
  Essential Nmap commands for network discovery, port scanning, and service enumeration.
- **reverse_shell/reverse_shell.md**  
  Reverse shell one-liners for various languages and platforms.
- **reverse_shell/upgrading_shell.md**  
  Techniques for upgrading simple shells to fully interactive TTYs.
- **web_assesment/XSS.md**  
  Basic XSS payloads for web application testing.
- **web_assesment/SQLI.md**  
  Common SQL Injection payloads for vulnerability testing.
- **web_enumeration/Technology_profiler.md**  
  Tools and commands to identify web technologies and frameworks.
- **web_enumeration/Web_discovery.md**  
  Tools and wordlists for web content and subdomain discovery.
- **wifi/wifi_crack.md**  
  Steps and commands for WiFi handshake capture and password cracking.
- **password_cracking/cracking.md**  
  Hash cracking tools, commands, and useful online resources.

## Project Structure

```
SecurityScripts/
├── nmap/
│   ├── extract_ports.py
│   └── nmap_commands.md
├── password_cracking/
│   └── cracking.md
├── reverse_shell/
│   ├── reverse_shell.md
│   └── upgrading_shell.md
├── web_assesment/
│   ├── SQLI.md
│   └── XSS.md
├── wifi/
│   └── wifi_crack.md
├──  web_enumeration/
│   ├── Technology_profiler.md
│   └── Web_discovery.md
```

## Features

- Ready-to-use command snippets for fast and effective security testing
- Well-documented options and usage notes
- Focus on practical, real-world scenarios

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Enrique720/SecurityScripts.git
    cd SecurityScripts
    ```

2. Browse the markdown files for commands and scripts.

3. Copy, modify, and use the commands as needed for your assessments.

> **Note:**  
> Many commands require root privileges. Use responsibly and only on systems you have permission to test.

## Ethics

This repository is provided for educational and authorized testing purposes only.