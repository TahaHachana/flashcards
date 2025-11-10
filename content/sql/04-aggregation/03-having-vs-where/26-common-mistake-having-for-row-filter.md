## Common Mistake HAVING for Row Filter

What's inefficient about this query and how do you improve it? `SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id HAVING customer_id IN (1,2,3);`

---

Inefficient: HAVING customer_id IN (1,2,3) filters after grouping all customers. Groups thousands of customers, then filters to 3. Better: WHERE customer_id IN (1,2,3) GROUP BY customer_id. This filters to 3 customers before grouping, so only 3 customer groups are created instead of thousands then discarded.

