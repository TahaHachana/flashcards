## Subqueries In FROM Clause

What is the purpose of subqueries in the FROM clause, and what is the key requirement for these subqueries?

---

Purpose: Treat a subquery like a temporary table that you can join to other tables. This separates complex logic (like aggregation) from the rest of the query.

Key requirement: FROM clause subqueries MUST be noncorrelated - they cannot reference columns from other tables at the same query level.

Why: They're executed first and their results held in memory for the duration of the query.

Example:
SELECT c.first_name, pymnt.total
FROM customer c
JOIN (SELECT customer_id, SUM(amount) total FROM payment GROUP BY customer_id) pymnt
  ON c.customer_id = pymnt.customer_id;

