## CTE Statement Scope Limitation

What does "statement scope" mean for CTEs, and how does this limit their usage?

---

Statement scope: CTEs exist only for the duration of the single statement where they're defined.

Example of limitation:
-- This works: CTE used in same statement
WITH totals AS (SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id)
SELECT * FROM totals;

-- This does NOT work: CTE doesn't exist in second query
WITH totals AS (SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id)
SELECT * FROM customer;
SELECT * FROM totals;  -- ERROR: totals doesn't exist

After the statement completes:
- CTE results are discarded
- Memory is freed
- Cannot be accessed by any subsequent query

Contrast with:
- Temporary tables: Session scope (persist until session ends)
- Views: Persist in database until dropped
- Subqueries: Also statement scope (same limitation)

Solution: Use temporary tables if you need data across multiple queries.

