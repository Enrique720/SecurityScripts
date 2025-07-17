#!/usr/bin/python3
'''
File to extract port information from nmap grepable output.
'''

import sys
import re

def extract_ports(nmap_output):
    ports = []
    for line in nmap_output.splitlines():
        # Use regex to find lines with port information
        match = re.search(r'(\d{1,5})\/(tcp|udp)', line)
        if match:
            port = match.group(1)
            protocol = match.group(2)
            ports.append((port, protocol))
    return ports

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_ports.py <nmap_output_file>")
        sys.exit(1)

    nmap_output_file = sys.argv[1]
    
    try:
        with open(nmap_output_file, 'r') as file:
            nmap_output = file.read()
            ports = extract_ports(nmap_output)
            for port, protocol in ports:
                print(f"{port}/{protocol}")
    except FileNotFoundError:
        print(f"File {nmap_output_file} not found.")
        sys.exit(1)