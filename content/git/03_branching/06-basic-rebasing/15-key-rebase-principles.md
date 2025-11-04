## Key Rebase Principles

What are the essential principles to remember about rebasing?

---

1. Rebase rewrites history by replaying commits on new base
2. Creates linear history (no merge commits)
3. Never rebase public/shared commits (golden rule)
4. Conflicts resolved per commit (more tedious)
5. Force push needed after rebasing pushed commits
6. Use `--force-with-lease` (safer than `--force`)
7. Rebase local work before pushing (clean history)
8. Merge for public branches (safer, preserves history)
9. Team agreement essential (establish policy)
10. `git rebase --abort` is your safety net

Rebasing is powerful but requires discipline!

