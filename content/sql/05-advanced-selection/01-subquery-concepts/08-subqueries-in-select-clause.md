## Subqueries In SELECT Clause

What are subqueries in the SELECT clause used for, and what is a key performance consideration?

---

Used to calculate values for each row in the result set.

Example:
SELECT 
  first_name,
  (SELECT SUM(amount) FROM payment p WHERE p.customer_id = c.customer_id) AS total
FROM customer c;

Performance consideration: If you need multiple calculated columns from the same table, you need multiple subqueries, which means accessing that table multiple times. This can be inefficient - joins or subqueries in FROM clause might be better.

