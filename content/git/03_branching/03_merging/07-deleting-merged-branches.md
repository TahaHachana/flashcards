## Deleting Merged Branches

How and when should you delete feature branches after merging?

---

Delete after successful merge:
```bash
git branch -d feature/login
```

Why delete:
- Keeps branch list clean
- Merged changes preserved in main
- Branch name no longer needed
- Can recreate from history if needed

Safe delete (`-d`): Only deletes if fully merged
Force delete (`-D`): Deletes even if unmerged (careful!)

Best practice: Delete feature branches immediately after merging.

