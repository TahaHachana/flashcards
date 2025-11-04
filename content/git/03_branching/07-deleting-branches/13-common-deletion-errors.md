## Common Deletion Errors

What are three common errors when deleting branches and their solutions?

---

1. "Branch not fully merged":
   - Check: `git branch --merged`
   - Force if intentional: `git branch -D branch`

2. "Cannot delete checked out branch":
   - Solution: `git switch main` first

3. "Remote ref does not exist":
   - Branch already deleted remotely
   - Cleanup local tracking: `git fetch --prune`

Always read error messages—they tell you exactly what's wrong and how to fix it.

