## INTERSECT Operator Purpose

What does the INTERSECT operator do, and what are common use cases?

---

INTERSECT returns only rows that appear in ALL result sets (the overlap).

Set theory representation:
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
A INTERSECT B: {3, 4}  -- Only rows in both

Key characteristics:
- Returns only rows that exist in all input sets
- If sets don't overlap, returns empty set
- Automatically removes duplicates (like UNION)

Example - Find people who are both customers AND actors:
SELECT first_name, last_name FROM customer
INTERSECT
SELECT first_name, last_name FROM actor;
-- Result: Only names appearing in both tables

Common use cases:
- Finding commonality between datasets
- Answering "which items appear in both A and B?"
- Verification queries ("do these queries return the same data?")

Note: MySQL 8.0+ supports INTERSECT. Earlier versions require workarounds using JOINs or EXISTS.

