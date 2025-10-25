## Basic Merge Command

What does `git merge branch-name` do and which branch must you be on?

---

`git merge branch-name` merges `branch-name` INTO your current branch.

Critical: You must be ON the branch you want to merge INTO (target branch).

Example:
```bash
git switch main           # Switch to target
git merge feature/login   # Merge feature INTO main
```

Common mistake: Being on the wrong branch. Always check with `git status` before merging.

