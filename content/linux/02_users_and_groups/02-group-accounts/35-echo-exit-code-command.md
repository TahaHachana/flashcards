## Echo Exit Code Command

How do you check if a command succeeded and what do the exit codes indicate?

---

Use `echo $?` to display the exit code of the last command. Exit codes indicate:
- 0 = Success
- Non-zero values = Various error conditions (specific meaning depends on the command)

This is useful for verifying command success and troubleshooting issues in both interactive sessions and scripts.

