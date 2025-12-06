## Set Operations Pitfall NULL Handling

How do set operations handle NULL values, and what unexpected behavior can occur?

---

NULL behavior in set operations:

Key rule: NULL = NULL in set operations (NULLs are treated as equal)

Example:
SELECT email FROM customer  -- Some emails are NULL
UNION
SELECT email FROM employee;  -- Some emails are NULL

Result: Multiple NULLs from both tables are consolidated to one NULL in the result.

Why this matters:

1. UNION removes duplicate NULLs (treats them as equal)
2. UNION ALL keeps all NULLs (includes each one)
3. INTERSECT finds NULL if it exists in both sets
4. EXCEPT can be affected by NULL presence

Potential issues:
- Losing information about how many NULLs existed
- Unexpected deduplication behavior
- Misinterpreting results (one NULL could represent many missing values)

Solutions:

1. Filter NULLs if they're problematic:
SELECT email FROM customer WHERE email IS NOT NULL
UNION
SELECT email FROM employee WHERE email IS NOT NULL;

2. Replace NULLs with meaningful values:
SELECT COALESCE(email, 'no-email') AS email FROM customer
UNION
SELECT COALESCE(email, 'no-email') AS email FROM employee;

Best practice: Be explicitly aware of NULL handling in your set operations.

