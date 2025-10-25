## Branch Visualization

How do you visualize branch structure and history in Git?

---

`git log --oneline --graph --all`

Shows ASCII graph of branches:
```
* d4e5f6g (HEAD -> feature/payment) Add payment
* c3d4e5f Add validation
| * b2c3d4e (feature/login) Add login
|/
* a1b2c3d (main) Initial commit
```

This displays:
- Current branch (HEAD)
- Where branches diverged
- Parallel development
- Branch relationships

Helps understand project structure and history.

