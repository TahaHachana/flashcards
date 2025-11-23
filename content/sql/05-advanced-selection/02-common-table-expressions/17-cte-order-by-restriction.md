## CTE ORDER BY Restriction

Why is ORDER BY typically not allowed in CTE definitions, and where should sorting occur?

---

ORDER BY typically not allowed in CTE definitions because order is meaningless for intermediate results.

This may not work:
WITH sorted_cte AS (
  SELECT * FROM customer ORDER BY last_name  -- May error or be ignored
)
SELECT * FROM sorted_cte;

Why: 
- CTEs are intermediate result sets, not final output
- Order is not guaranteed to be preserved when CTE is used
- Database may reorder for optimization
- ORDER BY in CTE serves no purpose

This DOES work (ordering in main query):
WITH customer_cte AS (
  SELECT * FROM customer  -- No ORDER BY
)
SELECT * FROM customer_cte ORDER BY last_name;  -- Order here

Correct approach:
- Perform ordering in the final SELECT
- Only order the actual result set you'll return
- CTE focuses on filtering and transforming, not ordering

Exception: Some databases (SQL Server) allow ORDER BY if combined with TOP or OFFSET/FETCH, but this is database-specific and not portable.

