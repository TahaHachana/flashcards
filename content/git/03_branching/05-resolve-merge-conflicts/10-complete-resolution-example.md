## Complete Resolution Example

Walk through a complete conflict resolution example.

---

```bash
# Attempt merge
git merge feature/login
# CONFLICT in auth.js

# Check status
git status
# both modified: auth.js

# Edit file (remove markers, fix conflict)
code auth.js

# Stage resolved file
git add auth.js

# Verify all resolved
git status
# All conflicts fixed

# Complete merge
git commit -m "Merge feature/login"

# Test
npm test
```

Key: Edit → Remove markers → Stage → Commit → Test

