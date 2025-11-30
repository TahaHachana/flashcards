## Removing Remotes

How do you remove a remote and when would you do it?

---

Remove remote:
```bash
git remote remove <name>
# or
git remote rm <name>
```

Example:
```bash
git remote remove upstream
```

When to remove:
- Remote no longer exists
- Changed hosting platform
- Cleanup after testing
- No longer need connection

Note: Only removes local reference, doesn't affect remote server.

