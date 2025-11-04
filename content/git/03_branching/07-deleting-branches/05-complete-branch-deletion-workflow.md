## Complete Branch Deletion Workflow

What are the steps for complete branch cleanup after merging?

---

1. Merge feature to main:
   ```bash
   git switch main
   git merge feature/payment
   ```

2. Delete local branch:
   ```bash
   git branch -d feature/payment
   ```

3. Delete remote branch:
   ```bash
   git push origin --delete feature/payment
   ```

4. Verify cleanup:
   ```bash
   git branch -a  # Check all branches
   ```

Two separate operations needed: local and remote deletion.

