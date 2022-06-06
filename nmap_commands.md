# Most useful scans for the discovery phase.  

---
## TCP SCAN

nmap -p- -sS --open --min-rate 5000 -vvv <ip> -n -Pn -oG allPorts

---
---

## UDP SCAN 

nmap -sU --top-ports 100 -T5 --open -v -n <ip> -oG udpScan

---

---
## Known open ports

nmap -p<port1,port2,...>  -sCV  <ip> -oN targeted

---

