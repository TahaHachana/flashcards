## Opening a File from Inside Vim — :e

How do you open a file for editing from within an already-running Vim session?

---

`:e filename`

This is especially needed when Vim was launched from a GUI environment without a filename. You can also use it to switch to a different file mid-session. If there are unsaved changes, Vim will warn you; use `:e! filename` to force the switch and discard changes.

