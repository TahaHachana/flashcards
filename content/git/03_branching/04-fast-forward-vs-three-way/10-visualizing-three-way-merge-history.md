## Visualizing Three-Way Merge History

What does history look like after a three-way merge?

---

`git log --oneline --graph --all`

Output:
```
*   g7h8i9j (HEAD -> main) Merge branch 'feature'
|\
| * f6g7h8i (feature) Add search
* | e5f6g7h Update README
|/
* a1b2c3d Initial commit
```

Characteristics:
- Branching visible (non-linear)
- Merge commit with two parents (`*` with two lines)
- Shows parallel development
- Full context preserved

Clearly shows work happened on separate branches simultaneously.

