## Login vs Non-Login Shells

What is the difference between login shells and non-login shells, which configuration files does each execute, and why does this distinction matter?

---

**Login Shells:**

**When They Occur:**
- Logging in via console (text mode)
- SSH into a remote system
- Using `su -` or `su -l` to switch users
- Explicit login shell: `bash -l` or `bash --login`

**Which Files Execute (in order):**
1. `/etc/profile` (system-wide)
2. First found of:
   - `~/.bash_profile`
   - `~/.bash_login`
   - `~/.profile`

**Purpose:**
- Set up the user environment
- Define environment variables (PATH, EDITOR, etc.)
- Run startup programs
- Load system-wide configurations

**Non-Login Shells:**

**When They Occur:**
- Opening a new terminal window in GUI
- Running `bash` command (without -l)
- Starting a subshell
- Most terminal emulators in graphical environments

**Which Files Execute:**
1. `/etc/bashrc` or `/etc/bash.bashrc` (system-wide)
2. `~/.bashrc` (user-specific)

**Purpose:**
- Apply interactive shell settings
- Load aliases and functions
- Set command prompt
- Configure history settings

**The Standard Solution:**

Most users configure `~/.bash_profile` to source `~/.bashrc`:

```bash
# In ~/.bash_profile:
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
```

**Why:** This ensures interactive settings (aliases, prompt, etc.) apply to BOTH login and non-login shells.

**Best Practice File Organization:**

**~/.bash_profile (Login shells):**
```bash
# Environment variables
export PATH=$PATH:/home/user/bin
export EDITOR=vim
export JAVA_HOME=/usr/lib/jvm/java-11

# Source .bashrc for interactive settings
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
```

**~/.bashrc (Interactive shells):**
```bash
# Aliases
alias ll='ls -alh'
alias gs='git status'

# Prompt
PS1="\u@\h:\w\$ "

# History
HISTSIZE=5000
export HISTCONTROL=ignoreboth

# Functions
mkcd() { mkdir -p "$1" && cd "$1"; }
```

**Check Shell Type:**
```bash
# Check if login shell
shopt -q login_shell && echo "Login shell" || echo "Not login shell"

# Or:
echo $0
# Output: -bash (login shell - note the dash)
# Output: bash (non-login shell)
```

