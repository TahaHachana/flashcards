## What is Rebasing

What is rebasing and how does it differ from merging?

---

Rebasing integrates changes by rewriting commit history. Instead of creating a merge commit, it moves (replays) your commits onto a different base.

Merge:
```
main: A---B---C---M
           \     /
feature:    D---E
```

Rebase:
```
main: A---B---C
               \
feature:        D'---E'
```

Key difference: Rebase creates new commits (D', E') with different hashes. Linear history, no merge commit.

