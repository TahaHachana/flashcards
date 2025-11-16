## Command History Variables

Explain the difference between HISTSIZE and HISTFILESIZE, and how command history storage works in Bash.

---

**Two Separate History Storage Locations:**

**1. In-Memory History (HISTSIZE)**
- Storage: RAM during current session
- Variable: `HISTSIZE`
- Access: Arrow keys, Ctrl+R
- Persistence: Lost when shell exits (unless saved)
- Purpose: Quick command recall during session

**2. Persistent History File (HISTFILESIZE)**
- Storage: `~/.bash_history` file on disk
- Variable: `HISTFILESIZE`
- Access: `history` command, file viewing
- Persistence: Survives reboots and logouts
- Purpose: Long-term command tracking

**Key Differences:**

| Aspect | HISTSIZE | HISTFILESIZE |
|--------|----------|--------------|
| Location | Memory (RAM) | Disk (~/.bash_history) |
| Survives | Session only | Reboots |
| Controls | In-memory buffer | Persistent file |
| Default | 500-1000 | 1000-2000 |

**How They Work Together:**

**Session Start:** Load history from `~/.bash_history` → Memory
**During Session:** Commands stored in memory (HISTSIZE limit)
**Session End:** Write memory to `~/.bash_history` (HISTFILESIZE limit)

**Configuration Examples:**

**View Current Settings:**
```bash
echo $HISTSIZE           # In-memory
echo $HISTFILESIZE       # File
```

**Standard Configuration:**
```bash
HISTSIZE=1000
export HISTFILESIZE=2000
```

**Power User Configuration:**
```bash
HISTSIZE=5000
export HISTFILESIZE=10000
```

**Security Configuration (Minimal History):**
```bash
HISTSIZE=0
export HISTFILESIZE=0
```

**Best Practice:**
Set `HISTFILESIZE ≥ HISTSIZE` to ensure all session commands are saved.

**Making Permanent:**
```bash
# Add to ~/.bashrc
echo 'HISTSIZE=5000' >> ~/.bashrc
echo 'export HISTFILESIZE=10000' >> ~/.bashrc
source ~/.bashrc
```

