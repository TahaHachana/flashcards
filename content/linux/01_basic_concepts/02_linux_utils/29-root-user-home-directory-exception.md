## Root User Home Directory Exception

Where is the root user's home directory located, and why is this different from standard users?

---

Root user's home directory is `/root`, NOT `/home/root`

**Why it's different:**
- Root is a special administrative account
- Separated from standard user home directories
- Located at top level of filesystem for system recovery purposes
- Ensures root has access even if `/home` partition fails to mount
- Clear distinction between administrative and standard user spaces

This is an important exception to remember when navigating the filesystem as root.

