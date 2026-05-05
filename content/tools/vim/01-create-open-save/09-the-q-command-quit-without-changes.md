## The :q Command — Quit Without Changes

When can you use `:q` to exit Vim, and what happens if you try to use it after making unsaved changes?

---

`:q` quits Vim and returns to the shell, but only if the buffer has no unsaved changes.

If there are unsaved changes, Vim refuses and shows:
```
E37: No write since last change (add ! to override)
```

To quit and discard changes you must use `:q!`.

