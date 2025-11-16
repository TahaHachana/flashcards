## PATH Variable Management

How does the PATH variable work, how do you modify it safely, and what is the critical security warning regarding PATH configuration?

---

**How PATH Works:**
PATH is a colon-separated list of directories that the shell searches (left to right) when you type a command.

**Example:**
```bash
echo $PATH
# Output: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# When you type 'ls':
# 1. Search /usr/local/bin (not found)
# 2. Search /usr/bin (not found)
# 3. Search /bin (FOUND - execute /bin/ls)
```

**Adding Directories to PATH:**

**Append (lower priority):**
```bash
export PATH=$PATH:/home/user/scripts
# New directory searched LAST
```

**Prepend (higher priority):**
```bash
export PATH=/home/user/bin:$PATH
# New directory searched FIRST
```

**Make Permanent:**
```bash
echo 'export PATH=$PATH:/home/user/scripts' >> ~/.bashrc
source ~/.bashrc
```

**CRITICAL SECURITY WARNING:**

**NEVER ADD THESE TO PATH:**
```bash
# DANGEROUS - DO NOT USE:
export PATH=$PATH:~              # Home directory
export PATH=$PATH:/home/user     # User's home
export PATH=$PATH:.              # Current directory
```

**Why This Is Dangerous:**
If an attacker places a malicious executable with a common name (like `ls`, `cd`, `cat`) in your home directory, the system might execute it automatically when you type that command, leading to malware auto-execution.

**Example Attack Scenario:**
```bash
# Attacker creates malicious 'ls' in your home directory
# You have home directory in PATH
# You type: ls
# System executes the malicious version instead of /bin/ls
```

**Safe Alternative for Local Scripts:**
Use `./` prefix to execute from current directory:
```bash
./myscript.sh        # Explicitly run from current directory
```

**Best Practice:**
- Keep PATH clean with only trusted system directories
- Never include user-writable directories
- Use explicit paths or `./` for local executables

