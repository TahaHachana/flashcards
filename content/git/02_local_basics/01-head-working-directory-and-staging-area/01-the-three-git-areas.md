## The Three Git Areas

Name the three areas Git uses to manage a project and describe the role of each.

---

1. **Working Directory (working tree)** — the actual files on your filesystem that you read and edit. Changes here are not yet recorded by Git.
2. **Staging Area (index)** — an intermediate buffer stored in `.git/index` where you deliberately accumulate file snapshots to include in the next commit.
3. **Repository (HEAD)** — the permanent record of committed snapshots. HEAD points to the most recent commit on the current branch.

