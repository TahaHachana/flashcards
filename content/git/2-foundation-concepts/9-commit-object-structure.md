# Commit Object Structure

How is a commit object structured and how can you inspect it?

---

A commit object points to a tree SHA, lists parent commit SHA(s), and includes author, date, and message.

Inspect it with:

```bash
git cat-file -p <commit_sha>
```
