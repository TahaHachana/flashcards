## Understanding Conflict Markers

What do the conflict markers mean in a file with merge conflicts?

---

Git adds special markers to show conflicting sections:

```
<<<<<<< HEAD
Changes from current branch (main)
=======
Changes from branch being merged (feature)
>>>>>>> feature-branch
```

Three sections:
1. `<<<<<<< HEAD`: Start, shows current branch changes
2. `=======`: Separator between versions
3. `>>>>>>> branch-name`: End, shows incoming changes

You must choose which to keep (or combine) and remove ALL markers.

