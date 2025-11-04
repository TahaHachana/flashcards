## Deleting Current Branch Error

What happens if you try to delete the branch you're currently on?

---

Error:
```bash
git branch -d feature/test
# error: Cannot delete branch 'feature/test' checked out at...
```

Solution: Switch to different branch first
```bash
git switch main
git branch -d feature/test
# Deleted branch feature/test
```

You cannot delete the branch you're currently on. HEAD must point to a different branch.

