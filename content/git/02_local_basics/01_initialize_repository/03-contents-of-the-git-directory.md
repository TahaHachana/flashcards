## Contents of the .git Directory

What critical information does the `.git` directory contain?

---

- HEAD (points to current branch)
- config (repository-specific settings)
- objects/ (Git's object database: commits, trees, blobs)
- refs/ (references to commits: branches and tags)
- hooks/ (scripts that run at certain Git events)
- Complete project history and metadata

Never manually edit `.git` contents—Git manages this automatically.

