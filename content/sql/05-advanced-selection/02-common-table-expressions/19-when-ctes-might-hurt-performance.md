## When CTEs Might Hurt Performance

In what scenarios might CTEs reduce performance, and what are alternatives?

---

Scenarios where CTEs might be slower:

1. Adding unnecessary complexity:
-- Overkill
WITH all_customers AS (SELECT * FROM customer)
SELECT * FROM all_customers WHERE state = 'CA';
-- Better
SELECT * FROM customer WHERE state = 'CA';

2. Preventing index usage:
-- CTE may prevent index use
WITH filtered AS (SELECT * FROM orders WHERE status = 'pending')
SELECT * FROM filtered WHERE customer_id = 123;
-- Better: Combined filters allow index
SELECT * FROM orders WHERE status = 'pending' AND customer_id = 123;

3. Large intermediate results without materialization:
-- If inlined, may scan large result multiple times
WITH large_cte AS (SELECT * FROM million_rows ...)
SELECT ... FROM large_cte WHERE ...
UNION ALL
SELECT ... FROM large_cte WHERE ...;
-- Consider temp table if not materialized

4. Hiding optimization opportunities:
-- Database can't see full picture to optimize
-- May miss join reordering or predicate pushdown opportunities

General principle: Use CTEs for clarity and organization, but don't overuse for trivial queries. Profile with realistic data.

