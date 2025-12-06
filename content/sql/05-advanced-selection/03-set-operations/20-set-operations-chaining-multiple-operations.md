## Set Operations Chaining Multiple Operations

How do you chain multiple set operations, and what are the precedence rules?

---

You can chain multiple set operations together:

Example - Three tables:
SELECT first_name, last_name FROM customer
UNION ALL
SELECT first_name, last_name FROM employee
UNION ALL
SELECT first_name, last_name FROM actor
ORDER BY last_name, first_name;

Execution: Operations performed left-to-right (or by precedence with mixing).

Precedence when mixing operators:
Standard ANSI SQL precedence:
1. INTERSECT (highest)
2. UNION and EXCEPT (equal)

Example without parentheses:
SELECT ... FROM A
UNION
SELECT ... FROM B
INTERSECT
SELECT ... FROM C;
-- Executes as: A UNION (B INTERSECT C)

Example with parentheses for clarity:
(SELECT ... FROM A
 UNION
 SELECT ... FROM B)
INTERSECT
SELECT ... FROM C;
-- Executes as: (A UNION B) INTERSECT C

Best practice: Use parentheses for clarity, don't rely on precedence rules. Explicit is better than implicit.

Note: Most queries use only one type of operator, so precedence rarely matters in practice.

