## .git/info/exclude vs .gitignore

What is .git/info/exclude and how does it differ from .gitignore?

---

.git/info/exclude is for personal ignore patterns you don't want to share:

```bash
# Edit exclude file
nano .git/info/exclude

# Add personal patterns
TODO-personal.txt
NOTES-*.md
```

Differences from .gitignore:
- NOT committed (stays local to your repo)
- Only affects YOUR local repository
- Useful for personal workflow files
- Same pattern syntax as .gitignore

Use for patterns specific to your workflow that teammates don't need.

