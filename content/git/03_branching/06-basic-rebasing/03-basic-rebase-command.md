## Basic Rebase Command

How do you rebase your current branch onto another branch?

---

```bash
# Switch to branch you want to rebase
git switch feature-branch

# Rebase onto target branch
git rebase main
```

This moves your feature branch commits on top of main's latest commit.

Typical workflow:
```bash
git switch feature
git rebase main        # Replay feature commits on main
git log --graph        # Verify linear history
```

