## User Deletion with Active Processes

What should you do if user deletion fails, and what command kills all processes for a user?

---

If user deletion fails, check for any running processes belonging to the user using the `ps` command. To kill all processes for a user before deletion, use:
`sudo killall -u {username}`

Linux prevents deletion of accounts with running processes, so you must halt them first.

