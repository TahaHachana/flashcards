## The Four File States in Git

What are the four possible states of files in Git?

---

1. Untracked: New files Git doesn't know about (use `git add` to track)
2. Tracked (Unmodified): Files in repository that haven't changed
3. Tracked (Modified): Files Git tracks that have been changed but not staged
4. Staged: Changes marked for next commit, ready to be committed

Check state with `git status`

