## Renaming Branches

How do you rename a Git branch?

---

Rename current branch:
```bash
git branch -m new-name
```

Rename specific branch:
```bash
git branch -m old-name new-name
```

Common use case (rename master to main):
```bash
git branch -m master main
```

The `-m` flag stands for "move" (rename). This is a local operation—remote branches need additional steps (covered later).

