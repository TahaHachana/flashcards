## The autowrite Option

What does the `autowrite` option do and when does it trigger an automatic save?

---

When `autowrite` (abbreviated `aw`) is set, Vim automatically writes the current buffer to disk before:
- Moving to the next file with `:n` (next).
- Running a shell command with `:!command`.

```
:set autowrite
:set noautowrite
```

This prevents accidental data loss when switching between files or shelling out.

