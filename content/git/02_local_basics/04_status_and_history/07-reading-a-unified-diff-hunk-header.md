## Reading a Unified Diff Hunk Header

What does the hunk header `@@ -4,7 +4,9 @@` mean in a `git diff` output?

---

The hunk header describes the line ranges shown in the old and new versions:

```
@@ -4,7 +4,9 @@

-4,7  → In the OLD file (a/): the hunk starts at line 4
         and covers 7 lines (lines 4–10).

+4,9  → In the NEW file (b/): the hunk starts at line 4
         and covers 9 lines (lines 4–12).

The difference (7 → 9) reflects 2 net lines added.
```

Within the hunk:
- Lines prefixed with `-` exist only in the old version (removed).
- Lines prefixed with `+` exist only in the new version (added).
- Lines with a leading space are unchanged context lines.

