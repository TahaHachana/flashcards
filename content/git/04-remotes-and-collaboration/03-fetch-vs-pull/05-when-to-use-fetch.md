## When to Use Fetch

When should you use `git fetch` instead of `git pull`?

---

Use fetch when:
- Want to review changes before merging
- Working on something and don't want interruptions
- Checking multiple remotes
- Want full control over integration

Workflow:
```bash
git fetch origin
git log origin/main          # Review
git diff main origin/main    # Compare
git merge origin/main        # Merge when ready
```

Fetch is safer—read-only operation that lets you review first.

