## Basic WITH Clause Syntax

What is the basic syntax for defining a CTE, and what are the key rules for multiple CTEs?

---

Basic syntax:
WITH cte_name AS (
  SELECT ...
  FROM ...
  WHERE ...
)
SELECT ...
FROM cte_name;

Multiple CTEs:
WITH 
  first_cte AS (SELECT ...),
  second_cte AS (SELECT ...),
  third_cte AS (SELECT ...)
SELECT ...
FROM first_cte JOIN second_cte ...;

Key rules:
- Separate multiple CTEs with commas (,)
- No comma after the last CTE
- Each CTE must have a unique name
- CTEs are defined in order from top to bottom

