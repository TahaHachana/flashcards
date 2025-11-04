## groupmod and groupdel Exit Codes

What are the five main exit codes for `groupmod` and `groupdel` commands?

---

The five main exit codes for `groupmod` and `groupdel` are:
- 0: Success
- 2: Invalid command syntax
- 6: Specified group doesn't exist
- 8: Can't remove user's primary group (for `groupdel`)
- 10: Can't update group file

Use `echo $?` to display the exit code of the last command.

