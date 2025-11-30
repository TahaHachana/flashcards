## What is git pull

What does `git pull` do and what is it equivalent to?

---

`git pull` downloads changes from remote AND immediately integrates them into your current branch.

Equivalent to:
```bash
git pull = git fetch + git merge
```

Steps:
1. Runs `git fetch` (downloads changes)
2. Automatically merges into current branch
3. Updates working directory

Think: "Get the latest changes and merge them into my current work."

