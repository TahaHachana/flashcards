## userdel -r Option

What does the `-r` option do with the `userdel` command and what is the default behavior without it?

---

The `-r` option removes the user's home directory and mail spool when deleting the account. Without `-r`, the `userdel` command does NOT remove the user's home directory by default - the directory remains on the system. Use `sudo userdel -r username` to delete both the account and home directory.

