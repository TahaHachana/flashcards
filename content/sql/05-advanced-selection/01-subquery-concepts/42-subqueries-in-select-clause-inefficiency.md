## Subqueries In SELECT Clause Inefficiency

Why can multiple subqueries in the SELECT clause be inefficient, and what's the alternative?

---

Problem: Each subquery in SELECT accesses its table separately, causing redundant work.

Inefficient - Accesses customer table 3 times:
SELECT 
  (SELECT first_name FROM customer c WHERE c.customer_id = p.customer_id),
  (SELECT last_name FROM customer c WHERE c.customer_id = p.customer_id),
  (SELECT email FROM customer c WHERE c.customer_id = p.customer_id)
FROM payment p;

Why inefficient: 
- Same table accessed 3 times per row
- Same join condition evaluated 3 times per row
- If payment has 1000 rows → 3000 subquery executions

Efficient alternative - JOIN once:
SELECT c.first_name, c.last_name, c.email
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id;

Alternative 2 - Subquery in FROM:
FROM payment p
JOIN (SELECT customer_id, first_name, last_name, email FROM customer) c
  ON p.customer_id = c.customer_id;

Principle: Access each table the minimum number of times necessary.

