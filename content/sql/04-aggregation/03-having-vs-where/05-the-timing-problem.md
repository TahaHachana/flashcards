## The Timing Problem

Explain the "timing problem" that prevents WHERE from using aggregate functions.

---

The timing problem is that WHERE runs at Step 2 (after FROM), but aggregates are calculated at Step 4 (after GROUP BY). Timeline: FROM → WHERE (no aggregates yet) → GROUP BY → calculate aggregates → HAVING (aggregates exist) → SELECT. It's conceptually impossible to filter on something before it's calculated, like trying to grade students based on test scores before the test is given.

