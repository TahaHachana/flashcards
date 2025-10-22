## Force Adding Ignored Files

How do you add a file to Git that's listed in .gitignore?

---

Use the `-f` or `--force` flag:

```bash
git add -f ignored-file.txt
# or
git add --force ignored-file.txt
```

WARNING: Only do this if you're certain the file should be committed despite being ignored. This overrides the .gitignore rule.

Common use case: Committing a specific config file that matches a broader ignore pattern.

