## JOIN Mental Model Summary

Describe the mental model for understanding how JOINs work conceptually.

---

Think of JOINs as: (1) Start with the Cartesian product - all possible row combinations, (2) Apply the ON condition as a filter - keep only matching combinations, (3) For OUTER JOINs - preserve unmatched rows from specified table(s) with NULLs for the other side, (4) Result is a temporary combined dataset that you can then filter (WHERE), sort (ORDER BY), or aggregate.

