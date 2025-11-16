## Alias Persistence and Management

How do you make aliases persistent across sessions, remove them, and what are the scope limitations of aliases?

---

**Default Alias Behavior:**
- Exist only in current shell session
- Lost when you log out
- User-specific (not shared with other users)
- Not inherited by subshells

**Making Aliases Persistent:**

**Method 1: Add to ~/.bashrc (Recommended)**
```bash
# Edit .bashrc
vim ~/.bashrc

# Add aliases:
alias ll='ls -alh'
alias c='clear'
alias ..='cd ..'

# Save and apply
source ~/.bashrc
```

**Method 2: Create ~/.bash_aliases (Cleaner)**
```bash
# Create dedicated alias file
vim ~/.bash_aliases

# Add all your aliases here
alias ll='ls -alh'
alias du='du -h'
alias df='df -h'

# Ensure .bashrc sources this file:
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# Apply
source ~/.bashrc
```

**Removing Aliases:**

**Remove Single Alias:**
```bash
unalias myalias
```

**Remove Multiple Aliases:**
```bash
unalias ll la l
```

**Remove All Aliases:**
```bash
unalias -a
```

**Bypass Alias Temporarily (Without Removing):**
```bash
# Three methods:
\ls                      # Backslash prefix
/bin/ls                  # Full path
command ls               # Command builtin
```

**Viewing Aliases:**
```bash
alias                    # View all aliases
alias ll                 # View specific alias
type ll                  # Check if command is aliased
```

**System-Wide Aliases (All Users):**
```bash
# Requires root - affects everyone
sudo vim /etc/bashrc
# Or: /etc/bash.bashrc (distribution-dependent)

# Add aliases
alias ll='ls -alh'
```

**Scope Limitations:**
- Aliases don't work in non-interactive shells by default
- Not expanded in scripts unless `shopt -s expand_aliases` is used
- Better to use functions instead of aliases in scripts

