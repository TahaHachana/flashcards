## Recovering Deleted Branches

How do you recover a branch that was accidentally deleted?

---

If commits were merged: Safe, they're in main branch

If commits were NOT merged: Use reflog

Recovery steps:
1. Find commit hash:
   ```bash
   git reflog
   # c3d4e5f HEAD@{1}: commit: Add feature
   ```

2. Recreate branch:
   ```bash
   git branch feature/test c3d4e5f
   ```

Time limit: Reflog keeps history for ~30 days. After that, commits are garbage collected. Recover quickly!

