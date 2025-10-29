## Switching Between Standard Users with su

How do you switch from one standard user account to another using su, and why is the `-l` flag important?

---

**Command:** `su -l username` or `su - username`

**Example:** `su -l jsmith`

**Why `-l` (login) flag is important:**
- Starts new shell as login shell
- Loads target user's complete environment
- Changes to target user's home directory
- Without `-l`, current user's environment persists (like HOME variable), which can cause unexpected behavior and issues

