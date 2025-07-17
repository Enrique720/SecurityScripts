# Password Hash Cracking Cheat Sheet

A quick reference for cracking password hashes using popular tools and online resources.

---

## 1. John the Ripper

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=<hash_type> <hashfile>
```
- **Common hash types:** `raw-md5`, `raw-sha1`, `nt`, `bcrypt`, etc.
- To show cracked passwords:
    ```bash
    john --show <hashfile>
    ```

---

## 2. Hashcat

```bash
hashcat -m <mode> -a 0 <hashfile> /usr/share/wordlists/rockyou.txt
```
- **-m:** Hash mode (e.g., 0 = MD5, 1000 = NTLM, 1800 = sha512crypt, etc.)
- **-a 0:** Dictionary attack
- To see all hash modes:
    ```bash
    hashcat -h | grep -A20 "Hash modes"
    ```

---

## 3. Hydra (for online attacks)

```bash
hydra -l <user> -P /usr/share/wordlists/rockyou.txt <target> <protocol>
```
- **Example:** SSH brute-force  
    ```bash
    hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100
    ```

---

## 4. Medusa (for online attacks)

```bash
medusa -h <target> -u <user> -P /usr/share/wordlists/rockyou.txt -M <service>
```
- **Example:**  
    ```bash
    medusa -h 192.168.1.100 -u root -P /usr/share/wordlists/rockyou.txt -M ssh
    ```

---

## 5. Hash-Identifier (Identify hash type)

```bash
hash-identifier
```
- Interactive tool to help identify hash types.

---

## 6. Useful Online Hash Cracking & Analysis Websites

- [CrackStation](https://crackstation.net/)
- [Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/)
- [Hashes.com](https://hashes.com/en/decrypt/hash)
- [OnlineHashCrack](https://www.onlinehashcrack.com/)
- [HashKiller](https://hashkiller.co.uk/)

---

## Tips

- Always identify the hash type before cracking.
- Use the largest and most relevant wordlists available (e.g., [SecLists](https://github.com/danielmiessler/SecLists)).
- For salted hashes, make sure to provide the salt in the correct format for your tool.
- Never attempt to crack passwords without proper authorization.
