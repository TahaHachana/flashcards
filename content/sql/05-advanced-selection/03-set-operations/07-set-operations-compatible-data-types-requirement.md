## Set Operations Compatible Data Types Requirement

What are the data type requirements for set operations, and how do different databases handle type mismatches?

---

Rule: Corresponding columns must have compatible data types (or database must be able to convert one to the other).

Example error:
SELECT email, first_name, last_name FROM customer  -- email is VARCHAR
UNION
SELECT customer_id, first_name, last_name FROM actor;  -- customer_id is INT
-- ERROR in most databases: Can't stack text on number

Database-specific behavior:
- Strict (PostgreSQL, Oracle, SQL Server): Reject type mismatches
- Permissive (MySQL/MariaDB): May auto-convert types
- SQLite: Doesn't enforce types strictly

Best practice - Explicit casting:
SELECT email, first_name, last_name FROM customer
UNION
SELECT CAST(customer_id AS VARCHAR(50)), first_name, last_name FROM actor;

Why: Ensures predictable behavior across databases and makes intent clear.

Mental model: All items in a column must be the same "kind of thing" - you can't mix apples and numbers in the same column.

