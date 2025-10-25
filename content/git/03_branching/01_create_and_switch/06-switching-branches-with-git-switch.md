## Switching Branches with git switch

How do you switch branches with git switch and what happens to uncommitted changes?

---

Basic switch: `git switch branch-name`

With uncommitted changes:

Scenario 1: Changes don't conflict with target branch
- Git allows the switch
- Changes carry over to new branch

Scenario 2: Changes conflict with target branch
- Git prevents the switch
- Error: "Your local changes would be overwritten"
- Must commit, stash, or discard changes first

Modern command (Git 2.23+): `git switch` replaces `git checkout` for clarity.

