## The passwd Command

What is the `passwd` command, what are its primary options, and how is it used for password and account management?

---

**Purpose:** The `passwd` command manages user account passwords, including setting, locking, unlocking, and expiring passwords.

**Basic Usage:**
```bash
passwd                    # Change your own password
sudo passwd username      # Change another user's password (requires root)
```

**Primary Options:**

**-d** - Delete password and disable account
```bash
sudo passwd -d username
```
- Removes password completely
- Account becomes disabled
- **Destructive operation** - password cannot be recovered

**-e** - Expire password immediately
```bash
sudo passwd -e username
```
- Password expires right away
- User MUST change password at next login
- Cannot log in without changing password
- Used for: new accounts, security incidents, forced resets

**-l (lowercase L)** - Lock account
```bash
sudo passwd -l username
```
- Account temporarily disabled
- Adds `!` prefix to password hash in `/etc/shadow`
- Password remains intact but unusable
- Can be unlocked later with `-u`

**How locking works:**
```bash
# Before: kgarcia:$6$hash...:18900:0:99999:7:::
# After:  kgarcia:!$6$hash...:18900:0:99999:7:::
```

**-u** - Unlock account
```bash
sudo passwd -u username
```
- Removes `!` prefix from password hash
- Restores access with original password
- Reverses `-l` lock operation

**Practical Examples:**

**Example 1: Change Own Password**
```bash
passwd
# Prompts for current password, then new password twice
```

**Example 2: Admin Sets User Password**
```bash
sudo passwd newuser
# Sets password without knowing current password
```

**Example 3: Force New User to Change Password**
```bash
sudo useradd -m newuser
sudo passwd newuser
sudo passwd -e newuser
# User must change password at first login
```

**Example 4: Temporary Account Lock (Employee Leave)**
```bash
# Lock account
sudo passwd -l employee

# Later, unlock when they return
sudo passwd -u employee
```

**Example 5: Security Incident Response**
```bash
# Immediately expire compromised password
sudo passwd -e compromised_user

# Or lock account during investigation
sudo passwd -l compromised_user
```

**Example 6: Disable Old Account**
```bash
sudo passwd -d olduser
sudo chage -E 0 olduser
```

**Root Capabilities:**
- Root can change any user's password
- Root doesn't need to know current password
- Root can lock/unlock any account

