## .gitignore Placement Scope

List the four places where ignore rules can be defined in Git and describe the scope of each.

---

```
1. <repo>/.gitignore         Committed to the repo; shared with all
                             contributors. Affects the whole repository.

2. <subdir>/.gitignore       Committed; shared. Affects only that
                             directory and its descendants.

3. ~/.config/git/ignore      Global — applies to all repositories on
  (core.excludesFile)        your machine. Not committed anywhere.
                             For personal tooling (editors, OS files).

4. .git/info/exclude         Local to this repo on this machine.
                             Not committed; not shared. Highest
                             precedence within the working tree.
```

