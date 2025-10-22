## Untracking Already-Tracked Files

How do you stop tracking a file that's already committed, but keep it in your working directory?

---

Use `git rm --cached` (removes from Git but keeps file locally):

Remove specific file:
```bash
git rm --cached filename.txt
git commit -m "Stop tracking filename.txt"
```

Remove directory:
```bash
git rm -r --cached directory/
```

Remove all ignored files:
```bash
git rm -r --cached .
git add .
git commit -m "Remove all ignored files"
```

The `--cached` flag is critical—without it, the file is deleted from your filesystem.

