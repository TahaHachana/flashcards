## CTE Chaining Mechanism

How does CTE chaining work, and what are the rules for referencing between CTEs?

---

CTE chaining: Later CTEs can reference earlier CTEs defined in the same WITH clause.

Example:
WITH 
  cte1 AS (SELECT ... FROM table),           -- Base data
  cte2 AS (SELECT ... FROM cte1 WHERE ...),  -- Uses cte1
  cte3 AS (SELECT ... FROM cte2)             -- Uses cte2
SELECT ... FROM cte3;

Rules:
- Later CTEs CAN reference earlier CTEs
- Earlier CTEs CANNOT reference later CTEs (not yet defined)
- Non-recursive CTEs cannot reference themselves
- Creates a pipeline of transformations

Execution flow:
1. cte1 executes first
2. cte2 executes using cte1 results
3. cte3 executes using cte2 results
4. Main query uses cte3 results

Like functional programming: data flows through a series of transformations.

