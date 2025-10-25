## HEAD Pointer

What is HEAD in Git and what does it indicate?

---

HEAD is a special pointer that indicates which branch (and commit) you're currently on.

```
main    →  [commit C]
            ↑
          HEAD
```

HEAD always points to your current branch. When you switch branches, HEAD moves to point to the new branch. When you commit, the branch that HEAD points to moves forward.

Check HEAD location: `git status` or `cat .git/HEAD`

