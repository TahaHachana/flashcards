## When EXISTS Is Better Than IN

When is EXISTS preferable to IN, and why?

---

EXISTS is often better when:

1. Checking relationships with complex conditions:
-- EXISTS: Natural and clear
WHERE EXISTS (SELECT 1 FROM rental r WHERE r.customer_id = c.customer_id AND r.rental_date < '2005-01-01')

-- IN: Awkward and less clear
WHERE customer_id IN (SELECT customer_id FROM rental WHERE rental_date < '2005-01-01')

2. Subquery might return NULLs:
-- NOT IN breaks with NULLs
-- NOT EXISTS works correctly regardless

3. Performance with large result sets:
-- EXISTS can short-circuit (stop at first match)
-- IN might need to build entire list first

4. Semantic clarity:
-- "Does this relationship exist?" → EXISTS
-- "Is this value in this list?" → IN

General guideline: For existence checks, use EXISTS. For membership in a simple list, use IN.

