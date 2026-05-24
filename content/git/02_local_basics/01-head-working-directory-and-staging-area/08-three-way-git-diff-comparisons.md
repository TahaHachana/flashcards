## Three-Way git diff Comparisons

Complete the table:

```
Command              Compares _________ vs _________
git diff             ?                  ?
git diff --staged    ?                  ?
git diff HEAD        ?                  ?
```

---

```
Command              Compares _________________ vs _____________
git diff             Working directory          Staging area
                     (shows unstaged changes)

git diff --staged    Staging area               HEAD (last commit)
                     (shows what will be committed next)

git diff HEAD        Working directory           HEAD (last commit)
                     (shows all changes: staged + unstaged combined)
```

