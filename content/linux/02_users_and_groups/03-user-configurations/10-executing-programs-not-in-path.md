## Executing Programs Not in PATH

How do you execute programs or scripts that are not in the PATH variable, and why doesn't the shell search the current directory by default?

---

**The Problem:**
If a script or program is in your current directory but that directory isn't in PATH, the shell won't find it:

```bash
ls
# Shows: myscript.sh

myscript.sh
# Output: bash: myscript.sh: command not found
```

**Solutions:**

**1. Use ./ Prefix (Most Common)**
```bash
./myscript.sh
```

**What ./ Means:**
- `.` = current directory
- `/` = path separator
- `./myscript.sh` = "the file myscript.sh in the current directory"

**2. Use Absolute Path**
```bash
/home/kgarcia/scripts/myscript.sh
```

**3. Use Relative Path**
```bash
# If script is in subdirectory:
subdirectory/myscript.sh

# If script is in parent directory:
../myscript.sh
```

**4. Add to PATH (Permanent Solution)**
```bash
# Add directory to PATH
export PATH=$PATH:/home/kgarcia/scripts

# Now can run directly:
myscript.sh
```

**Execution Permission Required:**

Before ANY method works, the file needs execute permission:
```bash
# Check permissions
ls -l myscript.sh
# Output: -rw-r--r-- (not executable)

# Add execute permission
chmod +x myscript.sh
# Now: -rwxr-xr-x (executable)

# Then run
./myscript.sh
```

**Why Doesn't Shell Search Current Directory?**

**Security Reasons:**

**The Attack Scenario:**
```bash
# Attacker creates malicious script in shared directory
$ cd /tmp
$ cat > ls
#!/bin/bash
echo "Stealing your data..."
rm -rf /important/files
^D

$ chmod +x ls

# Victim comes along
$ cd /tmp
$ ls          # If current dir was in PATH, runs malicious 'ls'
```

**Security Best Practice:**
The current directory (`.`) should NEVER be in PATH because:
- Prevents Trojan horse attacks
- Avoids accidental execution of malicious files
- Forces explicit intent (using `./`)
- Protects against social engineering

**NEVER Do This:**
```bash
# DANGEROUS - DO NOT USE:
export PATH=$PATH:.
export PATH=.:$PATH
```

**The ./ Requirement is a Feature:**
Requiring `./` forces you to explicitly state "I want to run THIS specific file in THIS directory" rather than accidentally running a different file with the same name.

**Practical Examples:**

**Running a Python script:**
```bash
python script.py           # Works (python is in PATH)
./script.py               # Works (explicit current directory)
script.py                 # Fails (script.py not in PATH)
```

**Running a compiled program:**
```bash
./myprogram              # Correct
myprogram                # Fails unless in PATH directory
```

**Best Practice:**
- Keep your own scripts in a dedicated directory (e.g., `~/bin`)
- Add that directory to PATH in `~/.bash_profile`
- For one-off or test scripts, use `./`
- Never add current directory (`.`) to PATH

