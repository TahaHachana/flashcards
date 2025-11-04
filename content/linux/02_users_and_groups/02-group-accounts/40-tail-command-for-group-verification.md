## Tail Command for Group Verification

How do you use the `tail` command to verify recent group and user changes?

---

Use:
- `tail /etc/group` - Displays the last 10 group entries (most recently added groups)
- `tail -n 3 /etc/group` - Displays the last 3 group entries
- `tail /etc/passwd` - Displays the last 10 user entries
- `tail -n 3 /etc/passwd` - Displays the last 3 user entries

This is useful for quickly verifying that new users or groups were created successfully.

