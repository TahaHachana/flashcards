## NOT IN Operator NULL Danger

What critical danger exists when using NOT IN with subqueries, and why does it occur?

---

Danger: If the subquery returns any NULL values, NOT IN may return unexpected results (empty set).

Why: SQL evaluates: value <> val1 AND value <> val2 AND value <> NULL

Since anything compared to NULL is unknown, the entire expression becomes unknown, and no rows pass the filter.

Example - Returns empty set if subquery contains NULL:
SELECT first_name
FROM customer
WHERE customer_id NOT IN (122, 452, NULL);
-- Result: Empty set

Solutions:
- Use NOT EXISTS instead
- Ensure subquery filters out NULLs: WHERE customer_id NOT IN (SELECT id FROM table WHERE id IS NOT NULL)

