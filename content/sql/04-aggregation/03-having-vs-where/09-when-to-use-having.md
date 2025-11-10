## When to Use HAVING

When should you use HAVING for filtering?

---

Use HAVING when filtering based on: (1) Aggregate function results (COUNT, SUM, AVG, etc.), (2) Conditions on grouped/summarized data, (3) Statistics about groups. Examples: HAVING COUNT(*) > 10, HAVING SUM(amount) > 1000, HAVING AVG(price) < 50. Use HAVING for group-level filters that need aggregate values.

