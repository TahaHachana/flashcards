## Merge Troubleshooting

What do these merge messages mean: "Already up to date", "Please commit your changes", "Automatic merge failed"?

---

"Already up to date":
- Current branch contains all commits from other branch
- Nothing to merge

"Please commit your changes or stash them":
- Working tree has uncommitted changes
- Solution: `git commit` or `git stash`

"Automatic merge failed; fix conflicts":
- Merge conflict detected
- Solution: Resolve conflicts manually (next topic)

Each message indicates what action is needed.

