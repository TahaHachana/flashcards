## What Is A Recursive CTE?

What is a recursive CTE, and what are its two essential parts?

---

A recursive CTE is a CTE that references itself, enabling queries over hierarchical or graph-structured data.

Two essential parts:

1. Anchor member (base case):
   - Starting point of recursion
   - Does NOT reference the CTE itself
   - Establishes initial rows

2. Recursive member (recursive case):
   - References the CTE itself
   - Builds on results from previous iteration
   - Joined with UNION ALL

Syntax:
WITH RECURSIVE cte_name AS (
  -- Anchor: Base case
  SELECT ... FROM base_table WHERE base_condition
  
  UNION ALL
  
  -- Recursive: References cte_name
  SELECT ... FROM base_table
  JOIN cte_name ON ...
  WHERE recursive_condition
)
SELECT * FROM cte_name;

Execution: Anchor runs once, then recursive member repeats until it returns no rows.

