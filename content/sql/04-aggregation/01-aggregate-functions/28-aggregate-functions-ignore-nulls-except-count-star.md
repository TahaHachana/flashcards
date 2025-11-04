## Aggregate Functions Ignore NULLs Except COUNT Star

Which aggregate function is the exception to the rule that aggregates ignore NULL values, and why?

---

COUNT(*) is the exception because it counts rows, not values. All other aggregates (COUNT(column), SUM, AVG, MIN, MAX) ignore NULL values and operate only on non-NULL values. COUNT(*) counts every row regardless of whether any columns in that row contain NULL, because it's asking "how many rows exist" not "how many values exist."

