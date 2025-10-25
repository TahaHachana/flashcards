## Recovering Lost Commits

How do you recover commits that were lost after leaving detached HEAD?

---

Use `git reflog` to find the lost commit:

```bash
git reflog
```

Output shows:
```
c3d4e5f HEAD@{0}: checkout: moving from d4e5f6g to main
d4e5f6g HEAD@{1}: commit: Fix  # Lost commit found!
```

Recover it:
```bash
# Option 1: Create branch at that commit
git branch recovered-work d4e5f6g

# Option 2: Checkout and create branch
git checkout d4e5f6g
git switch -c recovered-work

# Option 3: Cherry-pick to current branch
git cherry-pick d4e5f6g
```

