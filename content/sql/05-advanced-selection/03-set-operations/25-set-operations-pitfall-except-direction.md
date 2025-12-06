## Set Operations Pitfall EXCEPT Direction

Why is EXCEPT direction important, and how can you remember which way it works?

---

Critical rule: EXCEPT is directional. A EXCEPT B ≠ B EXCEPT A

Example showing difference:
-- Customers not in employees
SELECT name FROM customers EXCEPT SELECT name FROM employees;

-- Employees not in customers  
SELECT name FROM employees EXCEPT SELECT name FROM customers;

These return completely different results!

How to remember direction:

Mental model 1 - Subtraction:
A EXCEPT B = "A minus B" = "Start with A, subtract anything that's also in B"

Mental model 2 - Filtering:
A EXCEPT B = "From A, exclude anything in B"

Mental model 3 - Left to right:
"Take the left set, remove anything that appears in the right set"

Common mistake:
Using EXCEPT when you need both directions:
- Want: "Items only in A" OR "Items only in B"
- Wrong: A EXCEPT B (only gets "items only in A")
- Right: (A EXCEPT B) UNION (B EXCEPT A)

Best practice: Always explicitly think "which set am I starting from?" when using EXCEPT.

Oracle note: MINUS follows the same directional logic as EXCEPT.

