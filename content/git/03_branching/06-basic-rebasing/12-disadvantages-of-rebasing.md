## Disadvantages of Rebasing

What are four main disadvantages of using rebase?

---

1. **Rewrites history**: Dangerous for shared branches, can break collaboration
2. **More complex conflict resolution**: Conflicts per commit (may resolve same conflict multiple times)
3. **Harder to undo**: Can't simply revert, need `git reflog` to recover
4. **Loses merge context**: True parallel development not visible

Trade-off: Clean history vs. accurate history. Choose based on project needs and team preferences.

