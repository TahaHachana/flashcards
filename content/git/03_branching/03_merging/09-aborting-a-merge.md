## Aborting a Merge

How do you cancel a merge in progress and when should you use it?

---

Cancel merge:
```bash
git merge --abort
```

This:
- Cancels the merge operation
- Returns to pre-merge state
- Discards any conflict resolutions

Use when:
- You made a mistake (wrong branch)
- Conflicts are too complex
- You need to prepare differently
- You want to start over

Safe to use anytime during a merge before final commit.

