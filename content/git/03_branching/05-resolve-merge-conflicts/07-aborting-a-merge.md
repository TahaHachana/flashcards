## Aborting a Merge

How do you cancel a merge with conflicts and when should you do it?

---

Cancel merge:
```bash
git merge --abort
```

This:
- Cancels the merge operation
- Returns to pre-merge state
- Discards all conflict resolutions
- Safe to use anytime before final commit

Use when:
- Made mistakes in resolution
- Conflicts too complex
- Wrong branch merged
- Need to prepare differently

