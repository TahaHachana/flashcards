## Adding Users to Groups Command

What command is used to add a user to a group, and does this modify the user or the group?

---

The `usermod` command is used to add a user to an existing group. This operation modifies the USER object, not the group object. The syntax is: `usermod -options {argument}`

