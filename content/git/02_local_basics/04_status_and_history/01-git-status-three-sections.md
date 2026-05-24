## git status Three Sections

`git status` organises its output into three sections. Name each section and describe which files appear there.

---

```
1. Changes to be committed
   Files that are in the staging area (index) and differ from
   HEAD. These WILL be included in the next git commit.

2. Changes not staged for commit
   Tracked files that have been modified on disk since the last
   git add. These will NOT be in the next commit unless staged.

3. Untracked files
   New files Git has never been told about. Completely invisible
   to both git commit and git commit -a.
```

