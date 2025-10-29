## Force Password Change on First Login

Why would you force a user to change their password on first login, and what command accomplishes this? Describe a typical use case.

---

**Command**: `sudo passwd --expire username`

**Why Force Password Change**:

**Security Reasons**:
1. Initial account setup - admin sets temporary password
2. Password given verbally or in writing (insecure)
3. Security incident - ensure user controls password
4. Policy compliance - periodic forced changes
5. Temporary password security best practice

**What Happens**:
1. Administrator runs: `sudo passwd --expire username`
2. Password marked as expired
3. User can still log in once
4. Immediately prompted: "You must change your password now"
5. Cannot proceed until new password set
6. User now has password only they know

**Typical Use Case - New Employee**:
```bash
# 1. Admin creates account
sudo useradd -m jsmith

# 2. Admin sets temporary password
sudo passwd jsmith
[enters temporary password like "Welcome123"]

# 3. Admin expires password
sudo passwd --expire jsmith

# 4. Admin gives temporary password to user
# 5. User logs in with temporary password
# 6. System forces immediate password change
# 7. User sets personal password
```

**Security Best Practice**: Never let users keep passwords that were shared verbally/written or set by someone else.

