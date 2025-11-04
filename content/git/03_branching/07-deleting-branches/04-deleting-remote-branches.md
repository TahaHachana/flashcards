## Deleting Remote Branches

How do you delete a branch from a remote repository?

---

Delete remote branch:
```bash
git push origin --delete branch-name
```

Alternative syntax (older):
```bash
git push origin :branch-name
```

Example:
```bash
git push origin --delete feature/login
# - [deleted]         feature/login
```

Important: Deleting local branch doesn't automatically delete remote branch.

