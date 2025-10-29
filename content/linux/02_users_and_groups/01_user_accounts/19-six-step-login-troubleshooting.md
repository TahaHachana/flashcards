## Six-Step Login Troubleshooting

List the six-step troubleshooting checklist for user login failures in order, with the check method and solution for each.

---

**Follow in this order**:

1. **Account exists?**
   Check: `getent passwd username`
   Fix: `sudo useradd -m username`

2. **Password set?**
   Check: `sudo getent shadow username` (look for hash)
   Fix: `sudo passwd username`

3. **Forgotten password?**
   Check: User reports can't log in, review failed attempts
   Fix: `sudo passwd username`

4. **Password expired?**
   Check: `sudo chage -l username` (check expiration date)
   Fix: `sudo passwd username`

5. **Account locked?**
   Check: `sudo passwd -S username` (look for 'L' status)
   Fix: `sudo passwd -u username` or `sudo usermod -U username`

6. **Account expired?**
   Check: `sudo chage -l username` (check account expires field)
   Fix: `sudo chage -E -1 username` (never expires) or set new date

**Principle**: Start with most basic checks, progress systematically.

