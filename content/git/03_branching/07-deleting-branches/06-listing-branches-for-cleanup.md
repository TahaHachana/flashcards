## Listing Branches for Cleanup

How do you list merged and unmerged branches to decide what to delete?

---

Merged branches (safe to delete):
```bash
git branch --merged
```

Unmerged branches (review before deleting):
```bash
git branch --no-merged
```

Delete all merged branches except main:
```bash
git branch --merged | grep -v '\*\|main\|master' | xargs git branch -d
```

Always verify merged status before bulk deletion.

