## Detached HEAD Best Practices

What are best practices for working with detached HEAD?

---

GOOD uses:
- Read-only inspection: `git checkout a1b2c3d`, look around, `git switch main`
- Quick testing: Check out old version, run tests, switch back
- Finding bugs: Examine historical states

AVOID:
- Making commits without creating a branch (you'll likely lose them)
- Long-term work in detached HEAD (always create a branch for real work)

Rule: If you're doing actual development, create a branch immediately with `git switch -c branch-name`

