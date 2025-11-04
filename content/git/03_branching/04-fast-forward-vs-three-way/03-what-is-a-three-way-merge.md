## What is a Three-Way Merge

What is a three-way merge and when does it occur?

---

A three-way merge happens when both branches have new commits since they diverged—no direct linear path exists.

Before:
```
main:    A --- B --- C --- E
              \
feature:       D --- F
```

After:
```
main:    A --- B --- C --- E --- M
              \                 /
feature:       D --- F ---------
```

Merge commit M has two parents: E (main) and F (feature). Git must combine changes from both branches.

Indicator: "Merge made by the 'recursive' strategy"

