## UNION Operator Purpose

What does the UNION operator do, and how does it handle duplicate rows?

---

UNION combines two result sets and removes duplicate rows.

Set theory representation:
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
A UNION B: {1, 2, 3, 4, 5, 6}  -- All unique rows

Key characteristics:
- Removes duplicate rows (rows identical across all columns)
- May automatically sort results (implementation-dependent)
- More expensive than UNION ALL (requires duplicate detection and removal)

Example:
SELECT first_name, last_name FROM customer WHERE first_name LIKE 'J%'
UNION
SELECT first_name, last_name FROM actor WHERE first_name LIKE 'J%';

If "Jennifer Davis" appears in both tables, it appears once in results.

Use when: You specifically need duplicates removed from combined results.

