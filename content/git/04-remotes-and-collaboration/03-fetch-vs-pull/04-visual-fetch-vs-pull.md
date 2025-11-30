## Visual Fetch vs Pull

Visually, what's the difference between fetch and pull when local is behind remote?

---

Before:
```
Remote (origin/main): A---B---C---D---E
Local (main):         A---B---C
```

After `git fetch`:
```
origin/main:          A---B---C---D---E
Local (main):         A---B---C  (still here)
```
You know about D and E, but they're not merged.

After `git pull`:
```
Remote:               A---B---C---D---E
Local:                A---B---C---D---E  (updated)
```
D and E are merged into your working directory.

