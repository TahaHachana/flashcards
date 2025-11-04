## Rebase vs Merge Comparison

What are the key differences between rebase and merge?

---

Rebase:
- Linear history (rewritten)
- New commit hashes created
- No merge commit
- Risky for public branches
- Cleaner, simpler history
- Conflicts per commit

Merge:
- Non-linear history (preserved)
- Original commits kept
- Merge commit created
- Safe for all branches
- Shows true history
- Conflicts resolved once

Choose based on: branch visibility, team policy, history preference.

