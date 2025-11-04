## Bulk Cleanup Strategy

What's a safe workflow for bulk branch cleanup?

---

1. List merged branches:
   ```bash
   git branch --merged
   ```

2. Review the list (ensure no important branches)

3. Delete all merged branches except main:
   ```bash
   git branch --merged | grep -v '\*\|main\|master' | xargs git branch -d
   ```

4. Cleanup remote tracking:
   ```bash
   git fetch --prune
   ```

5. Verify:
   ```bash
   git branch -a
   ```

Do this periodically (weekly/monthly) as maintenance.

