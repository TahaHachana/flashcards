## The /etc/login.defs File

What is the /etc/login.defs file, what are the four core password configuration settings it contains, and what is a critical limitation when modifying this file?

---

**Purpose:** `/etc/login.defs` is the system-wide configuration file that defines default account creation settings and password policies.

**Four Core Password Configuration Settings:**

**1. PASS_MAX_DAYS**
- Maximum days before password change required
- Example: `PASS_MAX_DAYS 90` (quarterly password changes)
- Forces regular password rotation

**2. PASS_MIN_DAYS**
- Minimum days before password can be changed again
- Example: `PASS_MIN_DAYS 1` (must wait 1 day)
- Prevents immediate password cycling back to old password

**3. PASS_WARN_AGE**
- Days before expiration to display warning
- Example: `PASS_WARN_AGE 7` (one week warning)
- Gives users advance notice to change password

**4. PASS_MIN_LEN**
- Minimum characters required for password
- Example: `PASS_MIN_LEN 12` (12-character minimum)
- Basic password length requirement
- **Note:** Often superseded by PAM configuration on modern systems

**Example Configuration:**
```bash
# View password settings
grep "^PASS" /etc/login.defs

# Typical output:
PASS_MAX_DAYS   90
PASS_MIN_DAYS   1
PASS_WARN_AGE   7
PASS_MIN_LEN    8
```

**Modifying the File:**
```bash
# Backup first
sudo cp /etc/login.defs /etc/login.defs.backup

# Edit with root privileges
sudo vim /etc/login.defs

# Modify settings
PASS_MAX_DAYS   120
PASS_MIN_DAYS   1
PASS_WARN_AGE   5
PASS_MIN_LEN    12
```

**CRITICAL LIMITATION:**

Changes to `/etc/login.defs` apply ONLY to:
- New user accounts created AFTER the change
- New passwords set AFTER the change

Changes DO NOT automatically affect:
- Existing user accounts
- Current passwords already in use

**Solution:** Use `chage` command to update existing users:
```bash
# Apply new policy to existing user
sudo chage -m 1 -M 120 -W 5 username
```

**Additional Settings in /etc/login.defs:**
- UID/GID ranges
- Home directory defaults
- Default shell
- Password encryption method
- Default umask

