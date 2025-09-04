# Content vs. Pathname Tracking

How does Git track content versus pathname?

---

Git tracks file content by blob hash, not filenames. On checkout, it reconstructs filenames from tree objects. Two files with identical content share the same blob SHA:

```bash
echo hello > a.txt
echo hello > b.txt
git hash-object a.txt
git hash-object b.txt  # same SHA-1 as a.txt
```
