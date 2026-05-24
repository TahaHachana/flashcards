## HEAD Relative References

What commit does each of the following resolve to, and what is the difference between `~` and `^`?

```
HEAD~1
HEAD~2
HEAD^2
```

---

```
HEAD~1  (same as HEAD~)
        → The first parent of the current commit (one step back
          in linear history). Works for all commits.

HEAD~2  → Two steps back (parent of the parent).
          Shorthand for HEAD~~.

HEAD^2  → The SECOND parent of the current commit.
          Only meaningful for merge commits, which have two parents.
          HEAD^1 is the first parent (same as HEAD~1).
```

**Rule of thumb:**
- `~N` — go back N generations along the **first-parent** chain.
- `^N` — select the **Nth parent** of a single commit (for merges).

