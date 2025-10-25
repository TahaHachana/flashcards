## Pre-Merge Best Practices

What should you do before performing a merge?

---

Before merging:
1. Clean working tree: `git status` (commit or stash changes)
2. Update target branch: `git switch main && git pull`
3. Test feature branch (run tests, verify functionality)
4. Review changes: `git log main..feature` or `git diff main...feature`

Example:
```bash
git status              # Check clean
git switch main         # Switch to target
git pull               # Update
git merge feature      # Merge
```

Preparation prevents merge problems.

