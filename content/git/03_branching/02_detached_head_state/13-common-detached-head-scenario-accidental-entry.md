## Common Detached HEAD Scenario - Accidental Entry

What should you do if you accidentally enter detached HEAD state?

---

If you accidentally checked out a commit instead of a branch:

```bash
# Accidentally entered
git checkout a1b2c3d

# Simply switch back
git switch main
```

No harm done—just return to a branch. If you made any commits you want to keep, create a branch first:
```bash
git switch -c accidental-work
```

Check `git status` regularly to catch detached HEAD early.

