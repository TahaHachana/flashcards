## Unstaging Files

How do you unstage a file that was added to the staging area by mistake?

---

Modern Git (2.23+):
```bash
git restore --staged filename
```

Older Git:
```bash
git reset HEAD filename
```

This removes the file from staging but keeps your changes in the working directory. The file returns to "modified but not staged" state.

