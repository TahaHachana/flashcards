## Set Operations Cannot Sort Individual Queries

Why can't individual queries in a set operation have ORDER BY clauses, and where does ORDER BY go instead?

---

Rule: Individual queries cannot have ORDER BY clauses. Only the final combined result can be sorted.

Error example:
SELECT first_name, last_name FROM customer
ORDER BY last_name  -- WRONG
UNION
SELECT first_name, last_name FROM employee
ORDER BY last_name;  -- ALSO WRONG

Why: A set operation combines result sets, which are mathematically unordered sets. Sorting part of the result before combination makes no logical sense - like sorting half a deck before shuffling it together.

Correct approach:
SELECT first_name, last_name FROM customer
UNION
SELECT first_name, last_name FROM employee
ORDER BY last_name, first_name;  -- Sorts the entire combined result

What's being sorted: The entire combined result set, not individual components.

Formatting for clarity:
SELECT first_name, last_name FROM customer
UNION
SELECT first_name, last_name FROM employee
-- Sort the combined results:
ORDER BY last_name, first_name;

