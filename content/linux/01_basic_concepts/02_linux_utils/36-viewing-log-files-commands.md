## Viewing Log Files Commands

What are five essential commands for viewing and monitoring log files in Linux?

---

1. **`cat /var/log/syslog`** - View entire log file
2. **`tail /var/log/syslog`** - View last 10 lines (default)
3. **`tail -n 50 /var/log/syslog`** - View last 50 lines
4. **`tail -f /var/log/syslog`** - Follow log in real-time (continuous monitoring)
5. **`grep "error" /var/log/syslog`** - Search for specific term

Additional: `head -n 20` (first 20 lines), `less` (paginated viewing)

