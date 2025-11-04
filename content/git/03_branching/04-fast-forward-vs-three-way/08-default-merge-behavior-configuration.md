## Default Merge Behavior Configuration

How do you configure Git's default merge behavior?

---

Configure globally:

```bash
# Always create merge commits (no fast-forward)
git config --global merge.ff false

# Only allow fast-forward (fail otherwise)
git config --global merge.ff only

# Default behavior (ff when possible)
git config --global merge.ff true
```

Default: Git fast-forwards when possible, three-way merges when necessary.

Choose based on team policy and history preferences.

