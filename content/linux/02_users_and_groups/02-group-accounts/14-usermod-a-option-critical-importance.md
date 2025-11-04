## usermod -a Option Critical Importance

What does the `-a` option do in `usermod` and why is it critical?

---

The `-a` option appends the user to the group and maintains any existing group memberships. It is CRITICAL because if you do not use `-a`, the user is removed from all other supplementary groups and added only to the specified group. This mistake could have drastic security consequences as users can be members of multiple groups.

