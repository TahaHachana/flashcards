## CTE Nesting And Chaining

Can CTEs be nested, and what's the correct way to create dependent CTEs?

---

CTEs cannot be nested directly, but they can be chained.

This does NOT work (nesting):
WITH outer_cte AS (
  WITH inner_cte AS (SELECT ...)  -- ERROR: Can't nest CTEs
  SELECT * FROM inner_cte
)
SELECT * FROM outer_cte;

This DOES work (chaining):
WITH 
  inner_cte AS (SELECT ...),
  outer_cte AS (SELECT * FROM inner_cte)
SELECT * FROM outer_cte;

Chaining pattern:
- Define all CTEs in one WITH clause
- Separate them with commas
- Later CTEs reference earlier ones
- Creates a pipeline of transformations

Example:
WITH 
  step1 AS (SELECT ... FROM base_table),
  step2 AS (SELECT ... FROM step1 WHERE ...),
  step3 AS (SELECT ... FROM step2 JOIN other_table ON ...)
SELECT * FROM step3;

This is better than nesting because it's readable and follows natural top-to-bottom flow.

