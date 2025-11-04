## Checking for Existing Accounts

How can you check if a user account or group already exists before creating one?

---

Check the `/etc/passwd` file for user accounts or the `/etc/group` file for groups. You can use commands like:
- `grep username /etc/passwd` to check for a user
- `grep groupname /etc/group` to check for a group
- `grep :1000: /etc/passwd` to check for a specific UID
- `grep :1000: /etc/group` to check for a specific GID

Each user and group must have unique IDs and names.

