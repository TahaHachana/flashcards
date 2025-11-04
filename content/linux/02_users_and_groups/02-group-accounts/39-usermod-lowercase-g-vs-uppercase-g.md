## usermod Lowercase -g vs Uppercase -G

What is the critical difference between lowercase `-g` and uppercase `-G` in the `usermod` command?

---

Lowercase `-g` modifies the user's PRIMARY group (their default/initial login group). Use with caution as it changes the default group.

Uppercase `-G` adds the user to a SUPPLEMENTARY group (additional groups beyond primary). Must be used with `-a` to preserve existing supplementary memberships, otherwise all other supplementary groups are removed.

