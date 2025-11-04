## Why Three-Way Merge

Why is it called a "three-way" merge and what are the three reference points?

---

Git uses three reference points to perform the merge:

1. Common ancestor (B) - Last shared commit between branches
2. Target branch tip (E) - Current state of main
3. Source branch tip (F) - Current state of feature

```
        Base (B)
         /  \
    Main(E)  Feature(F)
         \  /
       Merge(M)
```

Git compares all three to determine the final merged state, resolving changes from both branches.

