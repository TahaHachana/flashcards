## usermod -G Option

What does the `-G` option do in the `usermod` command?

---

The `-G` option (uppercase G) specifies a supplementary group to which the user will be added. It should always be used with the `-a` option (`-aG`) to preserve existing group memberships. Using `-G` alone will remove the user from all other supplementary groups.

