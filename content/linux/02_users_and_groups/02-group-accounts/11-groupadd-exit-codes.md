## groupadd Exit Codes

What are the four main exit codes for the `groupadd` command and what do they mean?

---

The four main exit codes for `groupadd` are:
- 0: Success
- 2: Invalid argument syntax
- 4: GID not unique (Group ID already exists)
- 9: Group name not unique (name already exists)

You can check the exit code using `echo $?` after running the command.

