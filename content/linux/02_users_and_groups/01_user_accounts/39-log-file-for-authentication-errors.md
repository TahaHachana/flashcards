## Log File for Authentication Errors

Where can administrators find detailed logs of authentication attempts, both successful and failed, for troubleshooting login issues?

---

**Primary Authentication Log Files**:

**1. /var/log/auth.log** (Debian/Ubuntu):
```bash
sudo tail -f /var/log/auth.log
sudo grep username /var/log/auth.log
```
- Contains all authentication-related events
- Successful logins
- Failed login attempts
- sudo usage
- Account changes

**2. /var/log/secure** (Red Hat/CentOS/Fedora):
```bash
sudo tail -f /var/log/secure
sudo grep username /var/log/secure
```
- Similar to auth.log
- Red Hat family naming
- Same type of information

**What These Logs Show**:
- Login attempts (successful and failed)
- Source IP addresses
- Timestamps
- Authentication method (password, SSH key, etc.)
- PAM messages
- Account lockouts
- Password changes
- sudo commands

**Useful Commands**:

**Watch live authentication attempts**:
```bash
sudo tail -f /var/log/auth.log
```

**Search for specific user**:
```bash
sudo grep kgarcia /var/log/auth.log
```

**Find recent failed attempts**:
```bash
sudo grep "Failed password" /var/log/auth.log | tail -20
```

**Check for account lockouts**:
```bash
sudo grep "account locked" /var/log/auth.log
```

**Troubleshooting Workflow**:
1. User reports can't log in
2. Check: `sudo tail -50 /var/log/auth.log | grep username`
3. Look for: "Failed password", "account locked", "expired password"
4. Take appropriate action based on log messages

**Note**: Log file location varies by distribution - use appropriate path for your system.

