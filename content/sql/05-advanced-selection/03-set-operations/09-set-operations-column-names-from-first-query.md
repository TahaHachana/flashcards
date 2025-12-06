## Set Operations Column Names From First Query

Which query's column names and aliases appear in the final result of a set operation?

---

Rule: Only the FIRST query's column names and aliases are used in the final result.

Example:
SELECT first_name AS fname, last_name FROM customer
UNION
SELECT first_name, last_name AS lname FROM employee;

Result columns: fname, last_name
(The 'lname' alias from the second query is ignored)

Implication: Only bother with column aliases in the first SELECT statement.

Best practice:
SELECT first_name AS fname, last_name AS lname FROM customer
UNION
SELECT first_name, last_name FROM employee;
-- Result columns: fname, lname

Why this matters:
- Saves typing (don't alias in subsequent queries)
- Makes intent clear (aliases show what final result will look like)
- Subsequent queries can still use aliases for readability, but they won't affect the result

Mental model: The first query "defines the schema" for the combined result set.

