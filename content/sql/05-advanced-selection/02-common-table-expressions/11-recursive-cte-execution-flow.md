## Recursive CTE Execution Flow

Describe the execution flow of a recursive CTE with a concrete example.

---

Example - Employee hierarchy (employees table: id, name, manager_id):

WITH RECURSIVE employee_hierarchy AS (
  -- Anchor: CEO (no manager)
  SELECT id, name, manager_id, 1 as level
  FROM employees
  WHERE manager_id IS NULL
  
  UNION ALL
  
  -- Recursive: Find direct reports
  SELECT e.id, e.name, e.manager_id, eh.level + 1
  FROM employees e
  JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy;

Execution flow:
1. Iteration 1 (Anchor): Finds CEO (Alice) with level 1
2. Iteration 2 (Recursive): Finds Alice's direct reports (Bob, Carol) with level 2
3. Iteration 3 (Recursive): Finds Bob and Carol's reports (David, Emma, Frank) with level 3
4. Iteration 4: No more employees found → recursion stops
5. Final result: All employees with their hierarchy levels

Key: Each iteration uses results from previous iteration to find the next level.

