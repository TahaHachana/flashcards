## Practical Inspection Workflow

What is the recommended workflow for inspecting changes before committing?

---

1. `git status` - Check overall state (which files changed)
2. `git diff` - Review unstaged changes (what exactly changed)
3. `git add <files>` - Stage related changes
4. `git diff --staged` - Review what will be committed
5. `git commit -m "message"` - Commit
6. `git show` - Verify last commit

Always review before committing to catch mistakes and ensure logical commits.

