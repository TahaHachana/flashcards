## Detecting Merge Conflicts

How do you detect when a merge conflict has occurred?

---

When attempting merge:
```bash
git merge feature-branch
# CONFLICT (content): Merge conflict in file.txt
# Automatic merge failed; fix conflicts and then commit
```

Check status:
```bash
git status
# You have unmerged paths.
# Unmerged paths:
#   both modified:   src/app.js
```

Key indicators:
- `CONFLICT` message
- `Automatic merge failed`
- List of conflicting files in status

