## Account Storage Files

What are the critical differences between /etc/passwd and /etc/shadow files, and why are they separated?

---

**Two Files for Account Information:**

**1. /etc/passwd - Basic Account Information**

**Contents:**
- Username
- User ID (UID)
- Primary Group ID (GID)
- User information (GECOS field)
- Home directory path
- Default shell

**Example Entry:**
```
kgarcia:x:1001:1001:Kai Garcia:/home/kgarcia:/bin/bash
```

**Field Breakdown:**
1. kgarcia - Username
2. x - Password placeholder (actual password in /etc/shadow)
3. 1001 - UID
4. 1001 - Primary GID
5. Kai Garcia - Full name/comment (GECOS)
6. /home/kgarcia - Home directory
7. /bin/bash - Default shell

**Permissions:**
- World-readable (644)
- Any user can view this file
- Contains no sensitive information

**2. /etc/shadow - Password and Aging Information**

**Contents:**
- Encrypted passwords
- Password last change date
- Password aging policies
- Account expiration information

**Example Entry:**
```
kgarcia:$6$random$hash...:18900:1:90:7:::
```

**Field Breakdown:**
1. kgarcia - Username
2. $6$random$hash - Encrypted password
3. 18900 - Days since epoch of last password change
4. 1 - Minimum days between password changes
5. 90 - Maximum days before password expires
6. 7 - Warning days before expiration
7. (empty) - Inactivity period
8. (empty) - Account expiration date
9. (empty) - Reserved field

**Permissions:**
- Readable only by root (000 or 400)
- Contains sensitive password hashes
- Protected from unauthorized access

**Why the Separation?**

**Historical Context:**
Originally, everything was in /etc/passwd. This was a security problem because:
- Everyone could read encrypted passwords
- Attackers could perform offline password cracking
- Password hashes were publicly accessible

**Modern Security (Shadow Passwords):**
Separating into two files provides:

**1. Enhanced Security:**
- Sensitive password data protected (root-only access)
- Basic account info remains accessible (needed for system operations)
- Reduced attack surface

**2. Operational Necessity:**
- Many system operations need username/UID/GID information
- `/etc/passwd` provides this without exposing passwords
- Programs can look up user information without security risks

**3. Principle of Least Privilege:**
- Users can see basic account information (needed for system use)
- Only root can access password hashes (security-critical data)

**Viewing These Files:**

**Anyone Can View /etc/passwd:**
```bash
cat /etc/passwd
grep kgarcia /etc/passwd
```

**Only Root Can View /etc/shadow:**
```bash
sudo cat /etc/shadow
sudo grep kgarcia /etc/shadow
```

**Using getent (Preferred Method):**
```bash
# Query account databases (uses NSS)
getent passwd kgarcia
getent shadow kgarcia        # Requires root
```

