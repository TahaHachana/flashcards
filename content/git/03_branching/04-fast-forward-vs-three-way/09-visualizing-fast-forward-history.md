## Visualizing Fast-Forward History

What does history look like after a fast-forward merge?

---

`git log --oneline --graph`

Output:
```
* e4f5g6h (HEAD -> main, feature) Style button
* d3e4f5g Add button
* a1b2c3d Initial commit
```

Characteristics:
- Straight line (linear)
- No merge commits
- No branching visible
- Feature branch pointer at same location as main

Clean, chronological progression—looks like all work happened sequentially on one branch.

