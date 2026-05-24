## Git and GitHub Working Together

How do Git (local) and GitHub (remote) work together in a typical workflow?

---

```
Step | Tool   | Action
-----|--------|------------------------------------------
1    | Git    | Work locally: commit, branch, stage
2    | Git    | Push local repo to GitHub remote
3    | GitHub | Open pull request, review, run CI/CD
4    | Git    | Teammates pull changes to their local repos
```

GitHub is a **hosted remote** with collaboration tooling. You could replace it with any server that accepts Git pushes.

