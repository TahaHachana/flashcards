## Password Warning Period Purpose

What is the purpose of setting a password warning period with "passwd -w 14 username", and what experience does the user have?

---

**Purpose**: Give users advance notice before password expires, preventing surprise lockouts and reducing helpdesk calls.

**Command**: `sudo passwd -w 14 username`
Sets warning to start 14 days before password expiration

**How It Works**:
- Password set to expire in 90 days (example)
- Starting at day 76 (14 days before), user sees warning
- Warning displays at each login
- User can plan convenient time to change password

**User Experience**:

**Day 76 - First Warning**:
```bash
login: kgarcia
Password: ********

Warning: your password will expire in 14 days

[normal login proceeds]
```

**Day 85 - Closer Warning**:
```bash
Warning: your password will expire in 5 days
```

**Day 90 - Last Day**:
```bash
Warning: your password will expire in 0 days
```

**Day 91 - Expired**:
```bash
Your password has expired. Change it now.
```

**Benefits**:
- Users aren't surprised by expiration
- Can change password at convenient time
- Reduces emergency helpdesk password resets
- Improves user experience
- Maintains security while being user-friendly

**Common Values**:
- 7 days: One week notice
- 14 days: Two weeks (recommended)
- 30 days: Very generous notice

**Set with other policies**:
`sudo passwd -x 90 -n 7 -w 14 username`
(90 day max, 7 day min, 14 day warning)

