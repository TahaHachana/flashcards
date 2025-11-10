## Find Top Groups Pattern

How do you find the top N groups based on an aggregate value using HAVING and ORDER BY?

---

Pattern: GROUP BY to create groups, optionally HAVING to filter, ORDER BY aggregate DESC to sort by the aggregate value, LIMIT N to get top N. Example: SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id HAVING SUM(amount) > 0 ORDER BY total DESC LIMIT 10. Gets top 10 customers by spending.

