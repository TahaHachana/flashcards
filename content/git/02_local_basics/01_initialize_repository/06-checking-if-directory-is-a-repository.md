## Checking if Directory is a Repository

How can you check if a directory is already a Git repository?

---

Method 1: Check for `.git` folder: `ls -la | grep .git`

Method 2: Run `git status`:
- If it's a repo: Shows branch info and status
- If it's NOT a repo: "fatal: not a git repository (or any of the parent directories): .git"

The status command is the most reliable method.

