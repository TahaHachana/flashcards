## Distribution-Specific Root Account Handling

How do some Linux distributions (like Ubuntu) handle the root account differently, and what are the implications?

---

**Root Account Disabled by Default:**
- Root account exists but has no usable password
- Cannot use `su - root` (no password set)
- Forces exclusive use of sudo for administrative tasks

**Implications:**
- First user created typically given full sudo privileges
- Other users must be explicitly granted sudo access
- Eliminates risk of direct root login
- Enforces sudo's auditing and control mechanisms
- Encourages security best practices

**Security benefit:** Prevents password-based root access, making the system more secure.

