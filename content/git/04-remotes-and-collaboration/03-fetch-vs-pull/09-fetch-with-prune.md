## Fetch with Prune

What does `git fetch --prune` do and when should you use it?

---

```bash
git fetch --prune
# or
git fetch -p
```

Does:
- Fetches new data
- Removes references to deleted remote branches

Example:
```bash
# Someone deleted origin/old-feature remotely
git fetch --prune
# * [pruned] origin/old-feature
```

Configure automatic pruning:
```bash
git config --global fetch.prune true
```

Keeps local tracking branches in sync with remote.

