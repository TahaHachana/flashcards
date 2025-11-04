## Rebase Best Practices

What are key best practices for using rebase safely?

---

✅ Do:
- Rebase local, unpushed commits
- Rebase before pushing (clean history)
- Communicate with team about workflow
- Use for cleaning up local history

❌ Don't:
- Never rebase public/shared commits
- Don't rebase if others depend on your commits

Workflow:
```bash
# Safe: local cleanup before sharing
git rebase main
git push origin feature
```

Team agreement on merge vs rebase strategy is essential.

