## When to Use DISTINCT vs GROUP BY

When should you use DISTINCT versus GROUP BY?

---

Use DISTINCT when you want unique rows without any aggregates - simpler syntax for this purpose. Use GROUP BY when you need aggregate functions or statistics. Never use both together (redundant). Example: For unique states use SELECT DISTINCT state, but for counting customers per state use SELECT state, COUNT(*) ... GROUP BY state.

