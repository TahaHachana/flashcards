## Branch Deletion Best Practices

What are best practices for deleting branches?

---

Before deleting:
- Verify branch is merged: `git branch --merged`
- Check if anyone else is using it
- Confirm work is complete or abandoned
- Use safe delete (-d) by default

When to delete:
- Immediately after merging (keep repo clean)
- When abandoning work (signal it's dead)
- During cleanup sessions (periodic maintenance)

When NOT to delete:
- Active development branches
- Protected branches (main, develop, release)
- Branches others depend on

