## Recovering from Bad Rebase

How do you recover if a rebase goes wrong?

---

During rebase (not committed):
```bash
git rebase --abort  # Cancel and return to pre-rebase state
```

After rebase (committed):
```bash
git reflog          # Find commit before rebase
# e.g., d4e5f6g HEAD@{2}: commit: before rebase

git reset --hard HEAD@{2}  # Reset to that commit
```

Reflog keeps history of HEAD movements for ~30 days. Always check `git log` after rebase to verify before force pushing.

