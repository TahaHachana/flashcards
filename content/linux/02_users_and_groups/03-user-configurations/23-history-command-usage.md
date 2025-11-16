## History Command Usage

How do you use the `history` command to view, search, and re-execute commands, and what are the various methods for command recall?

---

**Viewing Command History:**

**Basic History Display:**
```bash
history
# Shows all commands with numbers

# Output example:
715  cd /var/log
716  tail -f syslog
717  grep "error" syslog
```

**View Last N Commands:**
```bash
history 20         # Show last 20 commands
history 5          # Show last 5 commands
```

**Search History:**
```bash
# Search for specific command
history | grep "docker"
history | grep "nginx"
```

**Re-Executing Commands:**

**Method 1: By Number**
```bash
# Execute command number 715
!715

# Example workflow:
history | grep "docker"
# Find: 832  docker ps -a
!832
# Re-executes: docker ps -a
```

**Method 2: Last Command**
```bash
!!                 # Execute last command

# Example:
sudo !!            # Run last command with sudo
```

**Method 3: By Pattern (Beginning)**
```bash
!grep             # Execute most recent command starting with "grep"
!cd               # Execute most recent "cd" command
!docker           # Execute most recent "docker" command
```

**Method 4: By Pattern (Containing)**
```bash
!?error           # Execute most recent command containing "error"
!?nginx           # Execute most recent command containing "nginx"
```

**Arrow Key Navigation:**

**Up Arrow:**
- Press once: Show previous command
- Press repeatedly: Scroll backward through history

**Down Arrow:**
- Scroll forward through history

**Ctrl+R (Reverse Search) - Most Powerful:**
```bash
# Press Ctrl+R
(reverse-i-search)`': 

# Type search term
(reverse-i-search)`dock': docker ps -a

# Press Ctrl+R again to find next match
# Press Enter to execute
# Press Esc to cancel and edit
```

**Advanced History Manipulation:**

**Access Previous Command Arguments:**
```bash
!$                # Last argument of previous command
!*                # All arguments of previous command
!^                # First argument of previous command

# Example:
cat /var/log/syslog
vim !$            # Opens: vim /var/log/syslog
```

**Substitute in Previous Command:**
```bash
^old^new          # Replace 'old' with 'new' in last command

# Example:
cat /var/log/messages
^messages^syslog  # Executes: cat /var/log/syslog
```

**Managing History:**

**Clear History:**
```bash
# Clear in-memory history (current session)
history -c

# Clear history file
cat /dev/null > ~/.bash_history

# Clear both
history -c && > ~/.bash_history
```

**Delete Specific Entry:**
```bash
# Delete command 715
history -d 715
```

**History Navigation Shortcuts:**

| Shortcut | Function |
|----------|----------|
| Up Arrow | Previous command |
| Down Arrow | Next command |
| Ctrl+R | Reverse search |
| Ctrl+P | Previous command (same as Up) |
| Ctrl+N | Next command (same as Down) |
| !! | Last command |
| !n | Command number n |
| !string | Last command starting with string |
| !?string | Last command containing string |

**Best Practices:**
1. Use Ctrl+R for quick search (most efficient)
2. Use arrow keys for recent commands
3. Use history numbers for specific commands
4. Configure HISTTIMEFORMAT for timestamps
5. Set adequate HISTSIZE and HISTFILESIZE

