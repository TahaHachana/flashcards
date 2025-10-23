## Root Account Security Best Practice

Why is it NOT recommended to log in directly as root, and what is the recommended security practice?

---

**Why not to log in as root:**
- Grants very broad, unrestricted permissions
- Increases risk of accidental system damage
- Makes it easier for malicious actors to compromise entire system
- No protection against typos or command errors

**Best practice:**
1. Log in as standard user
2. Use `su` or `sudo` only when root access needed
3. Perform specific administrative task
4. Exit back to standard user immediately

