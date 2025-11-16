## Troubleshooting Variable Issues

What are common problems when working with shell and environment variables, and how do you troubleshoot them?

---

**Common Variable Problems and Solutions:**

**Problem 1: Variable Not Available in Scripts or Child Processes**

**Symptom:**
```bash
MY_VAR="hello"
echo $MY_VAR        # Output: hello

bash                # Start subshell
echo $MY_VAR        # Output: (empty)
```

**Solution:**
```bash
# Use export to make it an environment variable
export MY_VAR="hello"
```

**Problem 2: Variable Changes Don't Persist After Logout**

**Symptom:** Variable works during session but disappears after logout/reboot.

**Solution:**
```bash
# Add to ~/.bashrc or ~/.bash_profile
echo 'export MY_VAR="permanent value"' >> ~/.bash_profile
source ~/.bash_profile
```

**Problem 3: PATH Changes Duplicated**

**Symptom:**
```bash
echo $PATH
# Shows: /usr/bin:/usr/bin:/usr/bin:/new/dir:/new/dir
```

**Cause:** PATH modified in wrong file or multiple times.

**Solution:**
```bash
# Remove duplicates, set PATH ONCE in ~/.bash_profile:
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/bin"

# Don't put PATH modifications in ~/.bashrc
```

**Problem 4: Variable Expansion Not Working**

**Symptom:**
```bash
DIR=/home/user
echo $DIRbackup        # Output: (empty)
```

**Solution:**
```bash
# Use curly braces to separate variable name
echo ${DIR}backup      # Output: /home/userbackup
```

**Problem 5: Spaces in Variable Assignment Causing Errors**

**Symptom:**
```bash
MY_VAR = "hello"
# Error: MY_VAR: command not found
```

**Solution:**
```bash
# NO spaces around = sign
MY_VAR="hello"        # Correct
```

**Problem 6: Variable Not Expanding in Single Quotes**

**Symptom:**
```bash
NAME="Maria"
echo 'Hello, $NAME'
# Output: Hello, $NAME (literal)
```

**Solution:**
```bash
# Use double quotes for variable expansion
echo "Hello, $NAME"
# Output: Hello, Maria
```

**Problem 7: Empty PATH After Modification**

**Symptom:**
```bash
export PATH=/new/dir
ls
# Error: ls: command not found
```

**Cause:** Overwrote PATH instead of appending to it.

**Solution:**
```bash
# ALWAYS append or prepend, never overwrite
export PATH=$PATH:/new/dir        # Append
export PATH=/new/dir:$PATH        # Prepend

# If PATH is broken, restore it:
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

**Troubleshooting Checklist:**

**For Variable Issues:**
```bash
# 1. Check if variable exists
echo $VARIABLE_NAME

# 2. Check if it's exported (environment variable)
export | grep VARIABLE_NAME
printenv VARIABLE_NAME

# 3. Check configuration files
grep -r "VARIABLE_NAME" ~/.bashrc ~/.bash_profile /etc/profile

# 4. Verify syntax (no spaces around =)
# 5. Use double quotes if variable contains spaces
# 6. Use curly braces for clarity: ${VARIABLE}
```

**For PATH Issues:**
```bash
# 1. View current PATH
echo $PATH

# 2. Check for duplicates
echo $PATH | tr ':' '\n' | sort | uniq -d

# 3. Find where PATH is being set
grep -rn "PATH=" ~/.bashrc ~/.bash_profile /etc/profile
```

