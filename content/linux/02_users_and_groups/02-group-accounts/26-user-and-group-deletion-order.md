## User and Group Deletion Order

What is the correct order for deleting users and their primary groups?

---

The correct order is:
1. Kill all user processes: `sudo killall -u username`
2. Delete the user account: `sudo userdel username` (or `sudo userdel -r username`)
3. Delete the primary group: `sudo groupdel groupname`

You cannot delete a user's primary group before deleting the user account.

