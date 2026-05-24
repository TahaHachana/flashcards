## The Unborn Branch

Right after `git init -b main`, HEAD says `ref: refs/heads/main`, but the branch does not yet exist. Why, and what causes it to appear?

---

The branch file (`refs/heads/main`) does not exist yet because Git creates branch ref files only when they have a commit to point to. Immediately after `git init` there are **no commits**, so there is nothing for the ref to record.

The branch file is created the moment you make your **first commit**:
```bash
git add .
git commit -m "Initial commit"
# → .git/refs/heads/main now exists and contains the new commit's SHA-1
```

Until then, the branch is called **unborn** and commands like `git log` or `git switch` will error or warn.

