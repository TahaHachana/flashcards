## Recursive CTE Infinite Loop Prevention

How can recursive CTEs create infinite loops, and what are strategies to prevent them?

---

Danger - Infinite loop without stopping condition:
WITH RECURSIVE infinite AS (
  SELECT 1 as n
  UNION ALL
  SELECT n + 1 FROM infinite  -- Runs forever!
)
SELECT * FROM infinite;

Prevention strategies:

1. Add termination condition in WHERE clause:
WITH RECURSIVE numbers AS (
  SELECT 1 as n
  UNION ALL
  SELECT n + 1 FROM numbers WHERE n < 100  -- Stops at 100
)
SELECT * FROM numbers;

2. Set maximum recursion depth (database-specific):
-- MySQL
SET SESSION cte_max_recursion_depth = 10;
-- SQL Server
OPTION (MAXRECURSION 10)

3. Track visited nodes (for graphs with cycles):
WITH RECURSIVE traversal AS (
  SELECT node_id, ARRAY[node_id] as path
  FROM graph WHERE node_id = 1
  UNION ALL
  SELECT g.node_id, t.path || g.node_id
  FROM graph g
  JOIN traversal t ON g.parent_id = t.node_id
  WHERE NOT (g.node_id = ANY(t.path))  -- Don't revisit
)
SELECT * FROM traversal;

Always include a stopping condition or depth limit.

