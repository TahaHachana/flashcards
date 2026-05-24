## What HEAD Points To

In normal (non-detached) operation, what is the chain of references that HEAD follows to reach a commit?

---

```
HEAD  →  refs/heads/<branch>  →  <commit SHA-1>
```

HEAD is a symbolic reference that points to the current **branch reference**, which in turn points to the latest **commit** on that branch. HEAD itself does not move when you make commits — the branch pointer advances, and HEAD keeps pointing to the same branch.

