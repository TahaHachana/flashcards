## How to Unstage a File

You staged `config.py` by mistake. How do you remove it from the staging area while keeping the changes in your working directory?

---

```bash
# Modern syntax (Git 2.23+)
git restore --staged config.py

# Classic syntax (still works in all versions)
git reset HEAD config.py
```

Both commands restore the staging area entry for `config.py` to the **HEAD version** (effectively removing the staged change), while leaving the file on disk **untouched**. The modifications remain in the working directory as unstaged changes.

