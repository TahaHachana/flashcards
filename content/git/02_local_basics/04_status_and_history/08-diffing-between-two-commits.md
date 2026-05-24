## Diffing Between Two Commits

Write the `git diff` command to see only the changes made to `src/app.py` between the commit three steps before HEAD and the commit two steps before HEAD.

---

```bash
git diff HEAD~3 HEAD~2 -- src/app.py
```

Breaking it down:
```
HEAD~3         → The older commit (three parents before HEAD)
HEAD~2         → The newer commit (two parents before HEAD)
-- src/app.py  → Limit the diff to this file only
                 (the -- separates refs from paths)
```

Without `-- src/app.py`, the diff would show all changed files between the two commits.

