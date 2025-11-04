## Statistical Summary Pattern

What's a common pattern for getting a complete statistical summary of a numeric column in one query?

---

Select multiple aggregate functions together: COUNT(*) for row count, MIN() for minimum, MAX() for maximum, AVG() for average, and SUM() for total. Example: SELECT COUNT(*), MIN(amount), MAX(amount), AVG(amount), SUM(amount) FROM payment. This gives a comprehensive statistical profile in a single query with one result row.

