# Web Content & Subdomain Discovery Cheat Sheet

A categorized list of tools for web content and subdomain discovery, with example commands and famous wordlists.

---

## Subdomain Discovery

### 1. **Sublist3r**

```bash
sublist3r -d <domain> -o subdomains.txt
```
- **Type:** Subdomain enumeration
- **Famous wordlist:** Built-in, but you can use SecLists: `subdomains-top1million-5000.txt`

### 2. **Amass**

```bash
amass enum -d <domain> -o amass_subs.txt
```
- **Type:** Subdomain enumeration
- **Famous wordlist:** Built-in, or use SecLists: `dns/subdomains-top1million-5000.txt`

### 3. **Assetfinder**

```bash
assetfinder --subs-only <domain> > assetfinder_subs.txt
```
- **Type:** Subdomain enumeration

---

## Directory & File Discovery

### 4. **WFUZZ**

```bash
wfuzz --hc=404 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt <url>/FUZZ
```
- **Type:** Directory and file brute-forcing
- **Famous wordlist:** `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`

### 5. **Gobuster**

```bash
gobuster dir -u <url> -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
```
- **Type:** Directory and file brute-forcing
- **Famous wordlist:** `/usr/share/wordlists/dirb/common.txt`

### 6. **Dirsearch**

```bash
python3 dirsearch.py -u <url> -e php,html,txt -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
- **Type:** Directory and file brute-forcing
- **Famous wordlist:** `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`

### 7. **FFUF (Fuzz Faster U Fool)**

```bash
ffuf -u <url>/FUZZ -w /usr/share/wordlists/dirb/common.txt -e php,txt,html -mc 200,204,301,302,307,401,403
```
- **Type:** Directory and file brute-forcing
- **Famous wordlist:** `/usr/share/wordlists/dirb/common.txt`

### 8. **Dirb**

```bash
dirb <url> /usr/share/wordlists/dirb/common.txt
```
- **Type:** Directory and file brute-forcing
- **Famous wordlist:** `/usr/share/wordlists/dirb/common.txt`

---

## Vulnerability & Content Scanning

### 9. **Nikto**

```bash
nikto -h <url>
```
- **Type:** Web server vulnerability scanning
- **Famous file:** Built-in database

---

## Wordlists

- `/usr/share/wordlists/dirb/common.txt`
- `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
- `/usr/share/wordlists/rockyou.txt`
- `SecLists` (https://github.com/danielmiessler/SecLists)

---

## Tips

- Use multiple tools and wordlists for thorough coverage.
- Adjust extensions and status code filters for your target.
- For authenticated fuzzing, check each tool's documentation for cookie/header options.

---

## Credits

- [SecLists Project](https://github.com/danielmiessler/SecLists)
- [WFuzz](https://github.com/xmendez/wfuzz)
- [Gobuster](https://github.com/OJ/gobuster)
- [dirsearch](https://github.com/maurosoria/dirsearch)
- [ffuf](https://github.com/ffuf/ffuf)
- [Nikto](https://github.com/sullo/nikto)
- [Dirb](https://github.com/v0re/dirb)
- [Sublist3r](https://github.com/aboul3la/Sublist3r)
- [Amass](https://github.com/owasp-amass/amass)
- [Assetfinder](https://github.com/tomnomnom/assetfinder)
