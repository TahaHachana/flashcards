## Exiting Detached HEAD Without Saving

How do you exit detached HEAD state if you want to discard any changes made?

---

Simply switch to a branch:
```bash
git switch main
# or
git switch -  # Return to previous branch
```

This abandons any commits made in detached HEAD (they become dangling commits).

Use this when:
- You were just inspecting old code
- You made experimental changes you don't want
- You accidentally entered detached HEAD

