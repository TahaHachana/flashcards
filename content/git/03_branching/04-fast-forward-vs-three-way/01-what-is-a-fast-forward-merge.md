## What is a Fast-Forward Merge

What is a fast-forward merge and when does it happen?

---

A fast-forward merge happens when the target branch hasn't changed since the feature branch was created—there's a direct linear path.

Before:
```
main:    A --- B
              \
feature:       C --- D
```

After:
```
main:    A --- B --- C --- D
```

Main pointer simply moves forward to D. No merge commit created because there's nothing to merge—just a pointer update.

Indicator: Git outputs "Fast-forward" message.

