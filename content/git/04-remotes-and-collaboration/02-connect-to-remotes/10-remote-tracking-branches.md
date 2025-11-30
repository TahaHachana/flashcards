## Remote Tracking Branches

What are remote tracking branches and how do you view them?

---

Remote tracking branches are local references to remote branches:
- Format: `<remote>/<branch>` (e.g., `origin/main`)
- Updated when you fetch/pull
- Read-only (can't commit directly)

View remote branches:
```bash
git branch -r
# origin/main
# origin/develop
```

View all branches (local + remote):
```bash
git branch -a
```

Check tracking relationships:
```bash
git branch -vv
```

