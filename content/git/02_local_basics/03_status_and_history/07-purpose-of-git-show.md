## Purpose of git show

What does `git show` do and what are common ways to use it?

---

`git show` displays detailed information about a specific commit, including metadata (author, date, message) and the full diff of changes.

Common usage:
- `git show`: Show last commit
- `git show HEAD`: Explicitly show last commit
- `git show a1b2c3d`: Show specific commit by hash
- `git show HEAD~3`: Show commit 3 commits ago
- `git show --stat a1b2c3d`: Show commit with stats, no diff

