## What is a Merge Commit

What is a merge commit and what makes it special?

---

A merge commit is created when divergent branches are merged. It's special because it has TWO parents (one from each branch):

```
    A --- B --- C (main)
           \     \
            D --- E (feature)
                   \
                    M (merge commit)
```

Merge commit M has:
- Parent 1: C (from main)
- Parent 2: E (from feature)
- Default message: "Merge branch 'feature-name'"

This preserves complete history of both branches.

