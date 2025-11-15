## NULL Handling In Subqueries Best Practices

What are best practices for handling NULLs in subqueries?

---

Best practices:

1. Dangerous pattern - Avoid:
WHERE customer_id NOT IN (SELECT customer_id FROM table);
-- Returns nothing if subquery contains NULL

2. Safer - Filter NULLs:
WHERE customer_id NOT IN (SELECT customer_id FROM table WHERE customer_id IS NOT NULL);

3. Best - Use NOT EXISTS:
WHERE NOT EXISTS (SELECT 1 FROM table WHERE table.customer_id = customer.customer_id);
-- Not affected by NULLs

Why NOT EXISTS is safer:
- EXISTS/NOT EXISTS check for row existence, not value equality
- NULL values don't cause the logical confusion that breaks IN/NOT IN
- More intuitive for "does this relationship exist?" questions

