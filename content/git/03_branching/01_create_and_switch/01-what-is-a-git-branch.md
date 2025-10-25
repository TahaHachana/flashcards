## What is a Git Branch

What is a Git branch and why are branches considered lightweight?

---

A branch is a movable pointer to a commit. It's not a copy of files or a new directory—just a 40-character SHA-1 hash stored in a file.

Branches are lightweight because:
- Creating a branch writes only a 41-byte file
- No disk space used (no file copying)
- Switching is instant
- You can create unlimited branches with no performance penalty

This makes branching cheap and encourages creating branches liberally.

