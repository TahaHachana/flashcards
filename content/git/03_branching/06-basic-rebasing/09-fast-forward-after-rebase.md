## Fast-Forward After Rebase

How does rebasing enable fast-forward merges?

---

After rebase, feature is directly ahead of main:

```bash
# Rebase feature onto main
git switch feature
git rebase main

# Result:
# main: A---B---C
#                \
# feature:        D'---E'

# Now merge (fast-forward)
git switch main
git merge feature

# Result:
# main: A---B---C---D'---E'
```

Clean linear history, no merge commit. This is a common workflow for maintaining linear project history.

