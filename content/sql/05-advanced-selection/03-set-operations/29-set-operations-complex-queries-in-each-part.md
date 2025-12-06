## Set Operations Complex Queries In Each Part

Can individual queries in a set operation be complex, and what's an example?

---

Yes! Each SELECT in a set operation can be arbitrarily complex: JOINs, subqueries, aggregation, CTEs, etc.

Example - Combining monthly and yearly aggregates:
WITH monthly_totals AS (
  SELECT customer_id, 
         DATE_TRUNC('month', order_date) AS month,
         SUM(amount) AS total
  FROM orders
  WHERE EXTRACT(YEAR FROM order_date) = 2024
  GROUP BY customer_id, DATE_TRUNC('month', order_date)
)
SELECT customer_id, month, total, 'Monthly' AS type
FROM monthly_totals

UNION ALL

SELECT customer_id, 
       NULL AS month, 
       SUM(amount) AS total, 
       'Yearly' AS type
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024
GROUP BY customer_id

ORDER BY customer_id, month NULLS LAST;

What this demonstrates:
- First query uses CTE with grouping
- Second query has different aggregation level
- Complex filtering and date functions
- Combined into single result set

Key insight: Set operations work at the result set level. Internal query complexity doesn't matter - only that results are compatible (same columns, types).

Flexibility: Each part can use different tables, JOINs, aggregations, whatever's needed.

