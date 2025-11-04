## Safe User Group Addition Example

What is the correct command to add user "jdeng" to the "sales" group while retaining membership in all other groups?

---

`usermod -aG sales jdeng`

The `-a` preserves existing group memberships, `-G` specifies the sales group, and jdeng is the username. Always use `-a` and `-G` together for safe supplementary group additions.

