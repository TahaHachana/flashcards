## Scalar Subquery Multiple Row Error Prevention

How do you prevent "subquery returns more than 1 row" errors when using scalar subqueries?

---

Prevention strategies:

1. Ensure subquery returns exactly one row:
   - Use aggregates: MAX(), MIN(), AVG(), SUM(), COUNT(*)
   - Add constraints: WHERE id = specific_value with unique constraint
   - Use LIMIT 1 (though this masks potential data issues)

2. If multiple rows are valid, use appropriate operator:
   - Wrong: WHERE country_id = (SELECT country_id FROM ...)
   - Right: WHERE country_id IN (SELECT country_id FROM ...)

3. Test subquery independently:
   -- Run this alone to verify result set
   SELECT country_id FROM country WHERE country <> 'India';
   -- If returns multiple rows, you need IN not =

Common mistake: Using = when data can legitimately return multiple rows. Design logic to match data reality.

