## Understanding diff Output

What do the symbols in git diff output mean?

---

```diff
--- a/file.txt    # Old version (before changes)
+++ b/file.txt    # New version (after changes)
@@ -1,4 +1,5 @@  # Line numbers (old file, new file)
-Line removed     # Line with - prefix was removed
+Line added       # Line with + prefix was added
 Unchanged        # No prefix = context line
```

Focus on `+` (additions) and `-` (deletions) to see actual changes.

