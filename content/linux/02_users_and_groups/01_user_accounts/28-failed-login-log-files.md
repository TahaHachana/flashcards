## Failed Login Log Files

Name the three log files used by login tracking commands and what each contains. Which command reads each file?

---

**1. /var/log/lastlog**:
- Contains: Last login time for each account
- Command: `lastlog`
- Format: Binary (not human-readable text)
- Shows: One entry per user, includes "Never logged in" for unused accounts

**2. /var/log/wtmp**:
- Contains: Complete history of all successful logins and logouts
- Command: `last`
- Format: Binary
- Shows: All login/logout events, session durations, remote access info

**3. /var/log/btmp**:
- Contains: Failed login attempts
- Command: `lastb` (requires root)
- Format: Binary
- Shows: Authentication failures, potential brute-force attacks

**Current Sessions** (not from file):
- Commands: `w` and `who`
- Source: System memory (live data)
- Shows: Currently logged-in users

**Note**: All binary format files require specific commands to read; cannot use cat or less directly.

