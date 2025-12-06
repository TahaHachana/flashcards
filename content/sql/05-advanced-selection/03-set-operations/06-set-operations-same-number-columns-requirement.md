## Set Operations Same Number Columns Requirement

Why must result sets in set operations have the same number of columns, and what happens if they don't?

---

Rule: Both result sets must have the same number of columns.

Example error:
SELECT first_name, last_name, email FROM customer  -- 3 columns
UNION
SELECT first_name, last_name FROM actor;  -- 2 columns
-- ERROR: Different column counts

Why this requirement exists:
SQL needs to know which column from the first set corresponds to which column in the second set. With different counts, alignment is impossible.

Think of it like stacking boxes:
- You can stack boxes that are the same width
- You can't stack a wide box on a narrow box (unstable/undefined)

Solution: Ensure all queries return the same number of columns:
SELECT first_name, last_name, email FROM customer
UNION
SELECT first_name, last_name, email FROM actor;  -- Now matches

Or add NULL placeholders:
SELECT first_name, last_name, email FROM customer
UNION
SELECT first_name, last_name, NULL AS email FROM actor;

