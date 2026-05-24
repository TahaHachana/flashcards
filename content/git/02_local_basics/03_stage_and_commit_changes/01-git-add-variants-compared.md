## git add Variants Compared

What is the difference between `git add .`, `git add -u`, and `git add -A`? Which one stages new untracked files?

---

```
git add .    Stages modifications, deletions, AND new untracked
             files — but only within the current directory and
             its subdirectories.

git add -u   Stages modifications and deletions for already-
             tracked files only. Does NOT stage new untracked
             files.

git add -A   Stages everything: modifications, deletions, and
             new untracked files across the ENTIRE repository,
             regardless of the current directory.
```

Both `git add .` and `git add -A` stage new files, but `-A` always covers the full repo while `.` is limited to the current subtree.

