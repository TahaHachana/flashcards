## Checking What's Ignored

What are three ways to check which files are ignored by Git?

---

1. `git status --ignored`: Shows all ignored files
2. `git check-ignore -v filename.txt`: Check if specific file is ignored and which rule matched
3. `git ls-files --ignored --exclude-standard --others`: List all ignored files

Example output from check-ignore:
```
.gitignore:3:*.txt    filename.txt
```
Shows file matched by rule on line 3 of .gitignore.

