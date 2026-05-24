## Three Core git diff Comparisons

Complete the table:

```
Command               Compares          vs
git diff              ?                 ?
git diff --staged     ?                 ?
git diff HEAD         ?                 ?
```

---

```
Command               Compares               vs
git diff              Working directory       Staging area
                      (unstaged changes —
                       what won't be committed yet)

git diff --staged     Staging area            HEAD (last commit)
  (= --cached)        (staged changes —
                       what WILL be committed next)

git diff HEAD         Working directory       HEAD (last commit)
                      (all changes: staged +
                       unstaged combined)
```

