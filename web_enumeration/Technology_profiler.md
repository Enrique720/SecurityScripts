# Web Technology Profiler Cheat Sheet

A list of tools and commands to identify technologies, frameworks, and platforms used by web applications.

---

## 1. WhatWeb

```bash
whatweb <url>
```
- **Description:** Identifies web technologies including CMS, frameworks, web servers, and more.
- **Example:**  
    ```bash
    whatweb https://example.com
    ```

---

## 2. Wappalyzer (CLI)

```bash
wappalyzer <url>
```
- **Description:** CLI version of the popular browser extension for technology detection.
- **Install:**  
    ```bash
    npm install -g wappalyzer
    ```
- **Example:**  
    ```bash
    wappalyzer https://example.com
    ```

---

## 3. BuiltWith

- **Description:** Online service for detailed technology profiling.
- **Website:** [https://builtwith.com/](https://builtwith.com/)
- **Usage:** Enter the target URL in the search bar.

---

## 4. Netcraft

- **Description:** Online tool for site reports and technology detection.
- **Website:** [https://sitereport.netcraft.com/](https://sitereport.netcraft.com/)
- **Usage:** Enter the target URL in the search bar.

---

## 5. Nmap HTTP Enum Scripts

```bash
nmap -p 80,443 --script http-enum <target>
```
- **Description:** Uses Nmap scripting engine to enumerate web applications and technologies.

---

## 6. EyeWitness

```bash
eyewitness -f <urls.txt> --web
```
- **Description:** Takes screenshots and gathers server header info, sometimes identifies technologies.
- **Install:**  
    ```bash
    git clone https://github.com/FortyNorthSecurity/EyeWitness.git
    ```

---

## Tips

- Combine multiple tools for more accurate results.
- Check HTTP headers and page source for clues about technologies.
- Browser extensions like Wappalyzer and BuiltWith are useful for quick checks.

---

## References

- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- [Wappalyzer](https://github.com/wappalyzer/wappalyzer)
- [BuiltWith](https://builtwith.com/)
- [Netcraft Site Report](https://sitereport.netcraft.com/)