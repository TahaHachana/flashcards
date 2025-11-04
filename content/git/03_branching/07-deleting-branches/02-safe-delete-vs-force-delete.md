## Safe Delete vs Force Delete

What's the difference between `git branch -d` and `git branch -D`?

---

`git branch -d branch-name` (lowercase d):
- Safe delete—only deletes if branch is fully merged
- Prevents accidental loss of work
- Git protects you from mistakes

`git branch -D branch-name` (uppercase D):
- Force delete—deletes regardless of merge status
- Use when abandoning unmerged work
- ⚠️ Warning: Unmerged commits may be lost

Default to `-d` for safety. Use `-D` only when certain.

