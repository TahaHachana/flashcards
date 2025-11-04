## Primary Group Deletion Restriction

What restriction exists when deleting a user's primary group?

---

You cannot delete a user's main/primary group without deleting the user account first. You must use the `userdel` command to remove the user account before you can delete their primary group. This is exit code 8 for the `groupdel` command.

