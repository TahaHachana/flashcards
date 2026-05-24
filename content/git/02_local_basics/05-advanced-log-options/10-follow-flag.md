## --follow Flag

What does `git log --follow -- src/auth.py` do that a plain `git log -- src/auth.py` does not?

---

`--follow` instructs Git to **track a file across renames**.

Without `--follow`, `git log -- src/auth.py` shows only commits that modified the file at the path `src/auth.py`. If the file was previously named `utils/auth.py` and later renamed, those older commits would be invisible.

With `--follow`, Git detects the rename event in the history and continues showing commits for the file under its previous names:

```bash
git log --oneline --follow -- src/auth.py
# Shows commits from when it was called utils/auth.py too
```

`--follow` works on a **single file only** — it cannot be used with directory paths or multiple files.

