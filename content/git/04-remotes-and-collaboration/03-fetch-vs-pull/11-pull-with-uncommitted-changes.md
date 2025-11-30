## Pull with Uncommitted Changes

What happens if you try to pull with uncommitted changes, and how do you fix it?

---

Error:
```bash
git pull
# error: Your local changes would be overwritten by merge.
# Please commit your changes or stash them.
```

Solutions:

Option 1: Commit
```bash
git add .
git commit -m "WIP"
git pull
```

Option 2: Stash
```bash
git stash
git pull
git stash pop
```

Always have clean working directory before pull.

