## groupadd -r Option

What does the `-r` option do in the `groupadd` command?

---

The `-r` option allows you to create a system group. System groups have GID numbering that starts at 101 (rather than 1000 for standard user groups) and are used for system-level operations. Example: `sudo groupadd -r sysgroup`

