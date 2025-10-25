## Saving Work from Detached HEAD

How do you save commits made in detached HEAD state?

---

Create a new branch from the current position:
```bash
git switch -c new-branch-name
```

This:
- Creates a new branch pointing to current commit
- Switches to that branch (HEAD now attached)
- Saves all commits you made in detached HEAD

Example:
```bash
# Made valuable commits while detached
git switch -c experimental-feature
# All commits now safe on 'experimental-feature' branch
```

