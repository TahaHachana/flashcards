## The :wq Command — Save and Quit

What is the difference between `:wq` and `:x` when saving and quitting?

---

Both `:wq` and `:x` write the file and quit, but:

- `:wq` — writes unconditionally, even if the file was not changed. This always updates the file's modification timestamp.
- `:x`  — writes only if the buffer has been modified. If nothing changed, it simply quits without touching the file or its timestamp.

This distinction matters when using build tools like `make`, which rely on file modification times.

