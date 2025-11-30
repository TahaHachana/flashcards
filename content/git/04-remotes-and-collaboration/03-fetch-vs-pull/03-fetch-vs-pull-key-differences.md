## Fetch vs Pull Key Differences

What are the key differences between `git fetch` and `git pull`?

---

Fetch:
- Downloads only
- No merge
- Working directory unchanged
- Safe (read-only)
- Use for: Review before merge

Pull:
- Downloads + merges
- Updates working directory
- Can cause conflicts
- Convenient
- Use for: Quick sync

Pull = fetch + merge (two operations in one)

