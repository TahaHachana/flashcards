## Run A Shell Command From Vim

What command runs a Unix command from inside Vim, shows its output, and returns you to editing without changing the buffer?

---

`:!command` — the `!` tells ex to start a shell and run the rest of the line. Press ENTER afterward to return to the same spot.

