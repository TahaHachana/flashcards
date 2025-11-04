## GROUP BY vs DISTINCT Overlap

How are GROUP BY and DISTINCT related, and when do they produce the same result?

---

When you don't use aggregate functions, GROUP BY and DISTINCT can produce identical results - both return unique combinations of the specified columns. Example: SELECT DISTINCT state, city and SELECT state, city ... GROUP BY state, city both return unique (state, city) pairs. However, GROUP BY is more powerful because it allows aggregates, while DISTINCT is simpler when you just want unique rows.

