## Pruning Remote Tracking Branches

What are remote tracking branches and how do you clean up stale references?

---

Remote tracking branches are local references to remote branches (e.g., `origin/feature/login`). When someone deletes a remote branch, your local tracking reference remains.

Check what would be pruned:
```bash
git remote prune origin --dry-run
```

Remove stale references:
```bash
git remote prune origin
# or
git fetch --prune
```

Configure to always prune:
```bash
git config --global fetch.prune true
```

