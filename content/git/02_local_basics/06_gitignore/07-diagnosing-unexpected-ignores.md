## Diagnosing Unexpected Ignores

A file you expect to be tracked keeps being ignored. Which command tells you exactly which `.gitignore` rule is responsible and where it is defined?

---

```bash
git check-ignore -v path/to/file.txt
```

The `-v` (verbose) flag prints the **matching rule**, the **file it came from**, and the **line number**:

```
.gitignore:3:*.log    path/to/file.log
```

This tells you: the rule `*.log` on line 3 of `.gitignore` is responsible.

Additional useful commands:
```bash
git status --ignored          # list ALL currently ignored files
git check-ignore -v "*.log"   # test a pattern, not just a specific file
```

