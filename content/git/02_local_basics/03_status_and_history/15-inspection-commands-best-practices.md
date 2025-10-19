## Inspection Commands Best Practices

What are the best practices for using Git inspection commands?

---

Status habits:
- Run `git status` before and after every operation
- Use `git diff --staged` before committing
- Check `git diff` before staging to catch mistakes

History review:
- Review `git log` regularly to understand project history
- Use `git show` to understand what a commit did
- Use `--oneline` for quick scans, `-p` for detailed review

These are read-only commands—use them liberally without fear.

