## Amending Commits

What does `git commit --amend` do and when should you use it?

---

`git commit --amend` replaces the last commit with a new one by:
- Combining staged changes with the previous commit
- Allowing you to change the commit message
- Creating a new commit that replaces the old one

WARNING: Only amend commits that haven't been pushed to a remote repository, as amending changes history.

Example: `git commit --amend -m "Corrected message"`

