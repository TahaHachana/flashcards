## Single vs Multi Column Grouping

What's the difference between single-column grouping and multi-column grouping in terms of what groups are created?

---

Single-column grouping creates one group per unique value in that column. Multi-column grouping creates one group per unique combination of values across all grouping columns. Example: GROUP BY state creates one group per state (50 groups in the US). GROUP BY state, city creates one group per state-city combination (potentially thousands of groups).

