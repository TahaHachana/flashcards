## Negation Pattern and Its Caveat

You write this `.gitignore`. Will `logs/important.log` be tracked? Why or why not, and how do you fix it?

```gitignore
logs/
!logs/important.log
```

---

**No — `logs/important.log` will still be ignored**, and this is a common trap.

When `logs/` is ignored as a directory, Git **stops descending into it entirely**. The negation `!logs/important.log` can never fire because Git never examines what is inside an ignored directory.

**Fix:** ignore the files inside the directory, not the directory itself:

```gitignore
logs/*.log
!logs/important.log
```

Now Git traverses `logs/`, ignores all `.log` files there, but keeps `important.log` tracked.

