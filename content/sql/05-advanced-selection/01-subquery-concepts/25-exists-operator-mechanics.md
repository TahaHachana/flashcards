## EXISTS Operator Mechanics

How does the EXISTS operator work, and what should the subquery SELECT?

---

EXISTS checks whether a subquery returns any rows at all. It doesn't matter what data or how many rows - just whether at least one row exists.

What should the subquery SELECT? It doesn't matter! By convention:
- SELECT 1 (most common)
- SELECT *
- SELECT any_columns

All produce the same result because EXISTS ignores the actual selected values.

Example:
WHERE EXISTS (SELECT 1 FROM rental r WHERE r.customer_id = c.customer_id 
              AND DATE(rental_date) < '2005-05-25');

Evaluates to TRUE if subquery returns one or more rows, FALSE if zero rows.

