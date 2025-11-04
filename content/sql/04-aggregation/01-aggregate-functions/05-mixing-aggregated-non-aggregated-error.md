## Mixing Aggregated and Non-Aggregated Columns Error

Why does this query fail: `SELECT customer_id, COUNT(*) FROM payment;`?

---

This fails because it tries to mix row-level data (customer_id) with summary-level data (COUNT) without explicit grouping. With implicit grouping, all rows form one group containing all customers mixed together. SQL doesn't know which customer_id value to display for this mixed group. The fix is to add GROUP BY customer_id to create separate groups for each customer.

