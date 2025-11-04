## Common Group Management Error Scenarios

What are five common error scenarios in group management and their solutions?

---

1. "Permission denied" - Use `sudo` or switch to root
2. "already exists" - Check `/etc/passwd` or `/etc/group` for conflicts
3. User deletion fails - Use `killall -u username` to kill processes first
4. Group deletion fails - Delete user first if it's their primary group
5. Home directory remains - Use `userdel -r username` to remove it

