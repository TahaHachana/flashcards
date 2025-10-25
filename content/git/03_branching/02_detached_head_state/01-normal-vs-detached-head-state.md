## Normal vs Detached HEAD State

What's the difference between normal (attached) HEAD and detached HEAD state?

---

Normal (Attached HEAD):
```
HEAD → main → [commit C]
```
- HEAD points to a branch name
- Branch points to a commit
- When you commit, the branch moves forward

Detached HEAD:
```
HEAD → [commit C]
     (no branch)
```
- HEAD points directly to a commit
- No branch is checked out
- Commits made are "dangling" (not on any branch)

