## Practical Command Aliases

Provide examples of practical, commonly-used command aliases and explain their benefits in real-world usage.

---

**Enhanced Directory Listings:**
```bash
alias ll='ls -alh'              # All files, long format, human-readable
alias la='ls -A'                 # All except . and ..
alias lr='ls -ltrh'              # Sort by time, newest last
alias lsize='ls -lSrh'           # Sort by size
```

**Quick Navigation:**
```bash
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias home='cd ~'
alias docs='cd ~/Documents'
```

**Human-Readable Disk Usage:**
```bash
alias du='du -h'                 # Disk usage in GB/MB
alias df='df -h'                 # Disk free in GB/MB
alias dus='du -sh'               # Summary only
```

**Limited Ping (Non-Continuous):**
```bash
alias ping='ping -c 5'
# By default, Linux ping runs continuously
# This alias stops after 5 packets automatically
```

**Safety Aliases (Prevent Accidents):**
```bash
alias rm='rm -i'                 # Confirm before delete
alias cp='cp -i'                 # Confirm before overwrite
alias mv='mv -i'                 # Confirm before overwrite
```

**Quick Screen Clear:**
```bash
alias c='clear'
alias cls='clear'
```

**Git Workflow:**
```bash
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'
```

**System Information:**
```bash
alias meminfo='free -h'
alias ports='netstat -tulanp'
alias topcpu='ps aux | sort -nrk 3 | head'
```

**Project Management:**
```bash
alias mk-proj='mkdir ~/projects'
alias goto-proj='cd ~/projects'
```

**Benefits:**
- Reduces repetitive typing
- Standardizes command options
- Prevents common mistakes
- Speeds up workflow
- Makes commands more user-friendly

