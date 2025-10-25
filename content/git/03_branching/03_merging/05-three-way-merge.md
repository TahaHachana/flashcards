## Three-Way Merge

What is a three-way merge and what three points does Git use?

---

When branches have diverged, Git performs a three-way merge using:

1. Common ancestor (base) - most recent shared commit
2. Current branch tip (ours) - where you are now
3. Branch being merged (theirs) - what you're merging in

```
        Base
         /  \
    Ours      Theirs
         \  /
        Merge
```

Git compares all three to determine the final result and creates a merge commit.

