## The Essential Log Combo

Write the single `git log` command that gives a compact, fully-labelled, visual graph of all branches in the repository, and explain what each flag contributes.

---

```bash
git log --oneline --graph --decorate --all
```

```
--oneline   → One line per commit: short hash + subject.
              Keeps the graph rows compact and readable.

--graph     → Draws ASCII art branch/merge lines to the left
              of each commit, showing how branches diverge
              and merge over time.

--decorate  → Annotates commits with the names of all refs
              (branches, tags, HEAD) that point to them.
              Without this you see hashes but not labels.

--all       → Includes commits from ALL refs (every local
              branch, remote-tracking branch, every tag),
              not just the currently checked-out branch.
```

