## What Are Set Operations

What are set operations in SQL, and how do they fundamentally differ from JOINs?

---

Set operations combine rows from two or more result sets, stacking them vertically.

Key distinction:
- JOINs: Add columns from one table to another (horizontal combination)
- Set operations: Add rows from one result set to another (vertical combination/stacking)

Mental model:
- Set operations: Stacking tables on top of each other (like stacking boxes)
- JOINs: Placing tables side by side (like placing boxes next to each other)

Example:
SELECT first_name, last_name FROM customers;  -- 599 rows
UNION
SELECT first_name, last_name FROM employees;  -- 34 rows stacked below

Result: Combined rows (vertical stacking), not combined columns (horizontal merging).

