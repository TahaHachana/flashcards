## Basic Conflict Resolution Steps

What are the 8 steps to resolve a merge conflict?

---

1. Identify conflicting files: `git status`
2. Open each conflicting file in editor
3. Locate conflict markers (`<<<<<<<`)
4. Decide resolution strategy (keep ours, theirs, combine, or new)
5. Remove ALL conflict markers completely
6. Stage resolved file: `git add file.txt`
7. Repeat for all conflicts
8. Complete merge: `git commit`

Critical: Must remove all `<<<<<<<`, `=======`, `>>>>>>>` markers!

