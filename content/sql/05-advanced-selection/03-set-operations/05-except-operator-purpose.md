## EXCEPT Operator Purpose

What does the EXCEPT operator do, and why does order matter?

---

EXCEPT returns rows from the first result set that are NOT in the second result set (set difference).

Set theory representation:
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
A EXCEPT B: {1, 2}  -- Rows in A but not in B

Key characteristics:
- ORDER MATTERS: A EXCEPT B ≠ B EXCEPT A
- Returns rows unique to the first set
- Automatically removes duplicates

Example:
SELECT first_name, last_name FROM customer
EXCEPT
SELECT first_name, last_name FROM actor;
-- Result: Customers who are NOT also actors (by name)

Oracle difference: Uses MINUS instead of EXCEPT (non-standard but same functionality).

Common use cases:
- Finding differences between datasets
- "Which customers haven't made purchases?"
- Data validation and quality checks

Mental model: "Subtraction" - first set minus the second set.

