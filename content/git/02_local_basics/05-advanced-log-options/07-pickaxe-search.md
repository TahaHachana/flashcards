## Pickaxe Search

What does `git log -S "authenticate_user"` do, and when would you use it?

---

`-S` is the **pickaxe** flag. It searches the history for commits that **added or removed** the exact string `"authenticate_user"` in any file's content (not just the commit message).

```bash
git log -S "authenticate_user" --oneline
```

Use it when you need to find:
- When a function, variable, or constant was first introduced.
- When it was removed.
- The commit responsible for a specific piece of code appearing or disappearing.

The related flag `-G "regex"` searches using a regular expression against the diff content, which is more powerful but slower.

