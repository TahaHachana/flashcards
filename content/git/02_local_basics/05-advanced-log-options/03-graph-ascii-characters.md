## --graph ASCII Characters

In `git log --graph` output, what do the characters `*`, `|`, `/`, and `\` represent?

---

```
*   → A commit node on the graph path

|   → A vertical branch line — the branch continues
      upward/downward without merging

/   → A branch line merging back together (converging)

\   → A branch line diverging (splitting off)
```

Example:
```
* abc  (main) latest commit
|\
| * def  (feature) feature commit
* | ghi  parallel commit on main
|/
* jkl  common ancestor
```

