## Correctness Reason for Both Clauses

Give an example where you MUST use both WHERE and HAVING for correct logic (not just efficiency).

---

Example: "Show active customers who have placed 10+ orders." SELECT customer_id, COUNT(*) FROM customers JOIN orders USING (customer_id) WHERE customers.status = 'active' GROUP BY customer_id HAVING COUNT(*) >= 10. WHERE filters to active customers (row-level attribute), HAVING filters to those with 10+ orders (aggregate). Using only HAVING would include inactive customers who have 10+ orders.

