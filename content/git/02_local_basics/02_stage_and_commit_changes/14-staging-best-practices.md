## Staging Best Practices

What are key best practices for staging and committing in Git?

---

Staging:
- Stage related changes together
- Review with `git diff --staged` before committing
- Use `git add -p` for partial staging of large changes

Committing:
- One commit = one logical change
- Commit often (small, focused commits)
- Test before committing (don't commit broken code)
- Write clear, descriptive messages
- Commit complete features, not work-in-progress

