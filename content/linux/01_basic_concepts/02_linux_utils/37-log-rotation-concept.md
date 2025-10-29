## Log Rotation Concept

What is log rotation, and why is it necessary in Linux systems?

---

**Log Rotation:** Automated process that manages log file sizes to prevent them from consuming all disk space.

**How it works:**
- Old logs are renamed and compressed (`.gz` extension)
- Very old logs are deleted
- New empty log file created
- Configured in `/etc/logrotate.conf` and `/etc/logrotate.d/`

**Example:**
- `/var/log/syslog` - current log
- `/var/log/syslog.1` - yesterday's log
- `/var/log/syslog.2.gz` - two days ago (compressed)
- `/var/log/syslog.3.gz` - three days ago (compressed)

**Why necessary:** Without rotation, logs would grow indefinitely and fill the disk.

