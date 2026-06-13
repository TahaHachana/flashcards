## Filter Quirk — Whole Lines Affected

If the cursor is mid-line when you filter, is only the partial text the motion covers passed to the command?

---

No. Entire lines are always affected — the full lines containing the start and end of the motion are filtered, not just the partial span.

