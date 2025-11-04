## Automatic Branch Deletion

How can you configure automatic branch deletion after merging on GitHub/GitLab?

---

GitHub:
- Settings → General → "Automatically delete head branches"
- Deletes feature branches after PR merge

GitLab:
- Settings → Repository → "Remove source branch after merge"
- Checkbox when creating merge request

This automates remote deletion, but local branches remain. Still need to:
```bash
git switch main
git pull
git branch -d feature/branch  # Delete local
git fetch --prune             # Cleanup tracking
```

