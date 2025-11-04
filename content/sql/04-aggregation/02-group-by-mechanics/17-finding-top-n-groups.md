## Finding Top N Groups

How do you use GROUP BY and ORDER BY together to find the top N groups based on an aggregate value?

---

Use GROUP BY to create groups, then ORDER BY an aggregate function with DESC and LIMIT. Example: SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id ORDER BY SUM(amount) DESC LIMIT 10. This groups by customer, calculates totals, sorts by those totals descending, and returns only the top 10 biggest spenders.

