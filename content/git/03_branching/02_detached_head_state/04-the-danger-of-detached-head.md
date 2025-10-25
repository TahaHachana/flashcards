## The Danger of Detached HEAD

Why is making commits in detached HEAD state risky?

---

When you commit in detached HEAD:
- The commit is created but no branch points to it
- If you switch away, the commit becomes "dangling"
- The commit has no reference and is hard to find
- Eventually gets garbage collected (deleted after ~30 days)

Example:
```bash
git checkout a1b2c3d  # Detached
git commit -m "Fix"   # Creates commit d4e5f6g
git switch main       # d4e5f6g is now dangling
```

Always create a branch to save commits made in detached HEAD.

