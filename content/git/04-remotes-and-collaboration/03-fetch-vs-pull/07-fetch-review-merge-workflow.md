## Fetch-Review-Merge Workflow

What's the safe fetch-review-merge workflow?

---

1. Fetch updates:
   ```bash
   git fetch origin
   ```

2. Review what's new:
   ```bash
   git log origin/main
   git diff main origin/main
   ```

3. Integrate (choose method):
   ```bash
   git merge origin/main    # Merge
   # or
   git rebase origin/main   # Rebase
   ```

This gives full control and prevents surprises.

