## Dangling Commits and Garbage Collection

What happens to dangling commits from detached HEAD, and how long do you have to recover them?

---

Dangling commits (not referenced by any branch or tag) are eventually garbage collected:
- Kept for about 30 days by default
- Then permanently deleted by `git gc`

Recovery before garbage collection:
```bash
git reflog              # Find lost commits
git fsck --lost-found   # Alternative method
git branch recovered <commit-hash>
```

This is why it's critical to save important commits to a branch immediately.

