## git diff Basic Usage

What's the difference between `git diff`, `git diff --staged`, and `git diff HEAD`?

---

- `git diff`: Shows unstaged changes (working directory vs staging area) - what you changed but haven't staged
- `git diff --staged` (or `--cached`): Shows staged changes (staging area vs last commit) - what will go into next commit
- `git diff HEAD`: Shows all changes (working directory vs last commit) - both staged and unstaged changes

Use `--staged` to review before committing.

