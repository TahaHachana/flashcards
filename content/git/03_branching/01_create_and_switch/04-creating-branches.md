## Creating Branches

What's the difference between `git branch feature-name` and `git switch -c feature-name`?

---

- `git branch feature-name`: Creates a new branch but stays on current branch
- `git switch -c feature-name`: Creates a new branch AND switches to it

`git switch -c` is equivalent to:
```bash
git branch feature-name
git switch feature-name
```

Use `git switch -c` when you want to immediately start working on the new branch.

