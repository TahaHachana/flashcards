## git show File Content at a Commit

How do you use `git show` to display the full content of a specific file as it existed at a particular commit — without seeing the diff?

---

Use the `<ref>:<path>` syntax:

```bash
git show HEAD:src/app.py          # file content at HEAD
git show v1.0:README.md           # file content at tag v1.0
git show abc1234:config/settings.py  # file content at a hash
```

This outputs the raw file content at that point in history, with no diff decoration. Useful for reading an old version of a file or piping it to another command.

