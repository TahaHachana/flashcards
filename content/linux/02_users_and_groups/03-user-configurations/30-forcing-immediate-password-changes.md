## Forcing Immediate Password Changes

How do you force a user to change their password at next login, and what are common scenarios where this is necessary?

---

**Two Methods to Force Password Change:**

**Method 1: Using `passwd -e`**
```bash
sudo passwd -e username
```
- Expires the password immediately
- User MUST change password at next login
- Cannot log in without changing password

**Method 2: Using `chage -d 0`**
```bash
sudo chage -d 0 username
```
- Sets "last password change date" to epoch (day 0)
- System treats password as expired
- Same effect as `passwd -e`

**What the User Experiences:**

**Login Attempt:**
```
login: username
Password: [enters current password]

You are required to change your password immediately (administrator enforced)
Current password: [enters current password]
New password: [enters new password]
Retype new password: [confirms new password]

Password changed successfully.
[normal login proceeds]
```

**User Cannot:**
- Log in without changing password
- Skip the password change
- Use the system until new password is set

**Common Scenarios:**

**1. New User Account Setup**
```bash
# Create user
sudo useradd -m newuser
sudo passwd newuser
# Force change at first login
sudo passwd -e newuser
```
**Use Case:** Administrator sets initial password, but user must choose their own.

**2. Security Incident (Compromised Password)**
```bash
sudo passwd -e affected_user
```
**Use Case:** Suspected password exposure, force immediate reset.

**3. Password Reset by Administrator**
```bash
# Admin resets forgotten password
sudo passwd username
# Force user to set their own password
sudo passwd -e username
```
**Use Case:** Help desk resets password, user must personalize it.

**4. Policy Compliance (Expired Passwords)**
```bash
# Force all users to comply with new password policy
for user in alice bob carol david; do
    sudo passwd -e $user
done
```
**Use Case:** Implementing new password requirements system-wide.

**5. Bulk Account Setup**
```bash
# Script to create multiple accounts
for user in user1 user2 user3; do
    sudo useradd -m $user
    echo "$user:Temp1234" | sudo chpasswd
    sudo passwd -e $user
done
```
**Use Case:** Create many accounts with temporary passwords.

**6. After System Compromise**
```bash
# Force all users to change passwords after breach
sudo passwd -e --all
```
**Use Case:** System-wide security incident response.

**Verification:**
```bash
# Check if password is expired
sudo chage -l username
# Output shows:
# Password expires: password must be changed
```

**Difference from Account Locking:**

**Expired Password (passwd -e):**
- User can log in
- Must change password during login
- Not locked out completely
- Can set new password themselves

**Locked Account (passwd -l):**
- User cannot log in at all
- Administrator must unlock
- User cannot fix it themselves
- Complete access denial

**Best Practice Workflow:**

**For New Users:**
```bash
sudo useradd -m newuser
sudo passwd newuser          # Set initial password
sudo passwd -e newuser       # Force change
```

**For Password Resets:**
```bash
sudo passwd username         # Reset to temporary password
sudo passwd -e username      # Force change at next login
# Communicate temporary password securely
```

**For Security Incidents:**
```bash
sudo passwd -e username      # Immediate expiration
# User forced to change at next login
```

**Key Point:** `passwd -e` is the standard, quickest way to force an immediate password change without locking the user out completely.

