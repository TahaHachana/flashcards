## Spotting Correlated Subqueries

How can you identify whether a subquery is correlated or noncorrelated?

---

Look for references to tables from the outer query inside the subquery. The correlation is usually in the WHERE clause.

Correlated example:
SELECT c.first_name
FROM customer c
WHERE EXISTS (SELECT 1 FROM rental r WHERE r.customer_id = c.customer_id);
                                                          -- References outer ↑

Noncorrelated example:
SELECT first_name
FROM customer
WHERE customer_id = (SELECT MAX(customer_id) FROM customer);
                     -- No reference to outer query ↑

If the subquery can run independently without the outer query, it's noncorrelated.

