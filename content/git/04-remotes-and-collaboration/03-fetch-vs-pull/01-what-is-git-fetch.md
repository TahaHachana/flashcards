## What is git fetch

What does `git fetch` do and what does it NOT do?

---

`git fetch` downloads commits, files, and refs from remote into your local repository.

Does:
- Downloads new commits and branches
- Updates remote tracking branches (origin/main)
- Connects to remote repository

Does NOT:
- Merge anything
- Modify working directory
- Change current branch

Think: "Get the latest info from remote, but don't touch my files yet."

