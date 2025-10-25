## What is a Merge Conflict

What causes a merge conflict and how do you detect one?

---

Conflict occurs when:
- Both branches modify the same part of the same file
- Git can't automatically determine which change to keep
- Manual intervention required

Detection:
```bash
git merge feature
# CONFLICT (content): Merge conflict in file.txt
# Automatic merge failed; fix conflicts and commit
```

Check status:
```bash
git status
# Unmerged paths:
#   both modified:   file.txt
```

(Conflict resolution covered in next topic)

