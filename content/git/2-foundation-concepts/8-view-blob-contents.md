# Viewing Blob Contents

How do you view raw blob contents in Git?

---

Use `git cat-file -p` with the blob’s SHA:

```bash
git cat-file -p <blob_sha>
```
