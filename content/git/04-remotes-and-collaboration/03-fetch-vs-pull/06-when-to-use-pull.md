## When to Use Pull

When should you use `git pull` instead of `git fetch`?

---

Use pull when:
- Starting work on clean branch
- Quick sync with remote
- Trust the remote changes
- Standard daily workflow

Example:
```bash
# Daily routine
git switch main
git pull origin main    # Get latest
git switch -c feature/new-work
```

Pull is convenient—one command for download + integrate.

