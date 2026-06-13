## The % Current-Filename Token

In a shell command run from Vim, what does `%` expand to, as in `:$r !spell %`?

---

`%` expands to the current filename. `:$r !spell %` reads the spell-check output of the current file in at the end of the buffer.

