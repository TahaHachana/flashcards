## Complete Query with Both Clauses

Write the pattern for a query that filters rows before grouping AND filters groups after aggregation.

---

SELECT columns, aggregates FROM tables WHERE <row conditions> GROUP BY columns HAVING <aggregate conditions>. Example: SELECT customer_id, COUNT(*) FROM orders WHERE status = 'completed' GROUP BY customer_id HAVING COUNT(*) > 10. This filters to completed orders first (row filter), then groups by customer, then shows only customers with 10+ orders (group filter).

