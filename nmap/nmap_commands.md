# Nmap: Essential Scans for the Discovery Phase

A collection of the most useful Nmap commands for initial reconnaissance and service enumeration.

---

## 1. Full TCP Port Scan

```bash
nmap -p- -sS --open --min-rate 5000 -vvv <target_ip> -n -Pn -oG allPorts
```
- **-p-**: Scan all 65535 TCP ports  
- **-sS**: SYN scan (stealthy and fast)  
- **--open**: Show only open ports  
- **--min-rate 5000**: Send packets quickly (adjust as needed)  
- **-vvv**: Increase verbosity  
- **-n**: No DNS resolution  
- **-Pn**: Treat all hosts as online (skip host discovery)  
- **-oG allPorts**: Output in grepable format to `allPorts`

---

## 2. Top 100 UDP Ports Scan

```bash
nmap -sU --top-ports 100 -T5 --open -v -n <target_ip> -oG udpScan
```
- **-sU**: UDP scan  
- **--top-ports 100**: Scan top 100 most common UDP ports  
- **-T5**: Insane speed (use with caution)  
- **--open**: Show only open ports  
- **-v**: Verbose  
- **-n**: No DNS resolution  
- **-oG udpScan**: Output in grepable format to `udpScan`

---

## 3. Targeted Service and Version Detection

```bash
nmap -p<port1,port2,...> -sCV <target_ip> -oN targeted
```
- **-p<ports>**: Specify ports (comma-separated)  
- **-sC**: Run default scripts  
- **-sV**: Version detection  
- **-oN targeted**: Output in normal format to `targeted`

---

## 4. Quick Host Discovery (Ping Sweep)

```bash
nmap -sn <target_network>
```
- **-sn**: Ping scan (host discovery only, no port scan)

---

## 5. Aggressive Scan (All-in-One)

```bash
nmap -A -T4 <target_ip> -oN aggressive
```
- **-A**: Enable OS detection, version detection, script scanning, and traceroute  
- **-T4**: Faster execution  
- **-oN aggressive**: Output in normal format to `aggressive`

---

## 6. Scan Specific Ports with Output

```bash
nmap -p 21,22,80,443 -sCV <target_ip> -oN specific_ports
```
- Replace ports as needed

---

## 7. Save Output in All Formats

```bash
nmap -p- -sS <target_ip> -oA full_tcp_scan
```
- **-oA**: Output in all formats (normal, XML, grepable) with basename `full_tcp_scan`

---

## Tips

- Replace `<target_ip>` or `<target_network>` with your actual target (e.g., `192.168.1.1` or `10.0.0.0/24`)
- Use `sudo` for scans requiring raw sockets (e.g., SYN or UDP scans)
- Adjust timing (`-T`), rate, and port ranges as needed for stealth or speed

---

