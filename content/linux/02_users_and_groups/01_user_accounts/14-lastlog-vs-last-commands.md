## lastlog vs last Commands

What is the difference between lastlog and last commands? What does each show and which log file does each read from?

---

**lastlog**:
- Shows LAST LOGIN ONLY for each account
- One entry per user
- Displays: username, terminal, source, timestamp
- Shows "Never logged in" for unused accounts
- Log file: /var/log/lastlog
- **Best for**: Identifying inactive accounts for deletion

**last**:
- Shows ALL login and logout events (complete history)
- Multiple entries per user
- Includes session duration and logout times
- Can filter by user, date, terminal
- Log file: /var/log/wtmp
- **Best for**: Comprehensive audits, security investigations, compliance reports

**Key Difference**: lastlog = snapshot (most recent), last = complete history

**Security Best Practice**: "It is good security practice to delete unused user accounts, and these tools help identify such accounts."

