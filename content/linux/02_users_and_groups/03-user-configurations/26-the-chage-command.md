## The chage Command

What is the `chage` command, what are its primary options, and provide examples of practical use cases for password management.

---

**Purpose:** The `chage` (change age) command manages password aging information for individual user accounts.

**Why It's Essential:** Required to update password policies for existing users (since `/etc/login.defs` only affects new accounts).

**Primary Options:**

**-l (list)** - Display current password aging information
```bash
chage -l kgarcia
```
Shows: last change date, expiration date, minimum/maximum days, warning period

**-M (uppercase M)** - Set maximum days between password changes
```bash
sudo chage -M 120 kgarcia
# Password must be changed every 120 days
```

**-m (lowercase m)** - Set minimum days between password changes
```bash
sudo chage -m 1 kgarcia
# Must wait 1 day before changing password again
```

**-W (uppercase W)** - Set warning days before expiration
```bash
sudo chage -W 5 kgarcia
# User warned 5 days before password expires
```

**-E (uppercase E)** - Set account expiration date
```bash
sudo chage -E 2025-12-31 kgarcia
# Account locks on December 31, 2025
```
Use `-E -1` to remove expiration date.

**-d** - Set last password change date (force immediate change with 0)
```bash
sudo chage -d 0 kgarcia
# Force password change at next login
```

**Practical Examples:**

**Example 1: View User's Password Settings**
```bash
sudo chage -l kgarcia
```

**Example 2: Implement Company Password Policy**
Company requires: 120 days max, 1 day min, 5 days warning
```bash
sudo chage -m 1 -M 120 -W 5 kgarcia
```

**Example 3: Force Immediate Password Change**
```bash
sudo chage -d 0 kgarcia
# User must change password at next login
```

**Example 4: Set Temporary Account (Contractor)**
Contractor's 6-month contract ends June 30, 2026
```bash
sudo chage -E 2026-06-30 contractor_user
sudo chage -M 60 contractor_user
```

**Example 5: Configure Multiple Settings at Once**
```bash
sudo chage -m 2 -M 90 -W 7 -E 2026-12-31 newuser
```

**Breakdown:**
- `-m 2`: Must wait 2 days between changes
- `-M 90`: Password expires every 90 days
- `-W 7`: 7-day warning before expiration
- `-E 2026-12-31`: Account expires on Dec 31, 2026

**Requires:** Root privileges (sudo) to modify other users.

