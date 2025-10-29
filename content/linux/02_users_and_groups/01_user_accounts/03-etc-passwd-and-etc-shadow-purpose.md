## /etc/passwd and /etc/shadow Purpose

Why are user accounts stored in TWO files (/etc/passwd and /etc/shadow) instead of one? What does each file contain and what are their access permissions?

---

**Historical Reason**: Passwords were originally in /etc/passwd (second field), but this file is world-readable (all users can read it), creating a security vulnerability.

**Modern Solution**:
- **/etc/passwd**: Contains account information (username, UID, GID, comment, home directory, shell). World-readable. Password field shows "x" as placeholder.

- **/etc/shadow**: Contains hashed passwords and password aging information. Only readable by root (administrator). Much more secure.

**Security Benefit**: Users can see account information they need, but password hashes remain protected from unauthorized access and offline attacks.

