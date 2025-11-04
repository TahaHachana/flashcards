## What You Can ORDER BY with GROUP BY

When using GROUP BY, what can you include in the ORDER BY clause?

---

You can ORDER BY: (1) columns that appear in GROUP BY, (2) aggregate functions, or (3) expressions involving grouped columns or aggregates. Examples: ORDER BY state (grouped column), ORDER BY COUNT(*) DESC (aggregate), ORDER BY state, num_customers DESC (combination). This lets you sort by the groups themselves or by their aggregated statistics.

