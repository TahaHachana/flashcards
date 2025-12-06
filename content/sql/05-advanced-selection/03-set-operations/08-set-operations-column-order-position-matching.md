## Set Operations Column Order Position Matching

How does SQL match columns in set operations, and why is this dangerous?

---

Rule: SQL matches columns by POSITION, not by NAME.

Dangerous example - Columns reversed:
SELECT first_name, last_name FROM customer
UNION
SELECT last_name, first_name FROM employee;  -- REVERSED!

Result: first_name column contains last names from employees
        last_name column contains first names from employees

Why dangerous: Query runs without error, but data is nonsensical because columns are misaligned.

Correct approach:
SELECT first_name, last_name FROM customer
UNION
SELECT first_name, last_name FROM employee;  -- Consistent order

When different column names is useful:
SELECT givenname, familyname FROM customers
UNION ALL
SELECT firstname, lastname FROM sorting;
-- Works because they're in the same logical positions (1st position = first name, 2nd position = last name)

Best practice: Visually align queries to ensure column order consistency.

