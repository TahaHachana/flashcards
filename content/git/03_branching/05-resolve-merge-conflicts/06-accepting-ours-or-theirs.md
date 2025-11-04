## Accepting Ours or Theirs

How do you quickly accept all changes from one side of a conflict?

---

Accept current branch (ours):
```bash
git checkout --ours file.txt
git add file.txt
```

Accept incoming branch (theirs):
```bash
git checkout --theirs file.txt
git add file.txt
```

For all files:
```bash
git checkout --ours .    # All ours
git checkout --theirs .  # All theirs
git add .
```

⚠️ Use carefully—resolves without reviewing individual changes.

