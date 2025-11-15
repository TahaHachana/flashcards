## Scalar Subquery Multiple Row Error

What happens if you use the = operator with a subquery that returns multiple rows? Why does this occur?

---

You get an error: "Subquery returns more than 1 row"

Why: A single value cannot be equated to a set of values. When you write:
WHERE country_id = (SELECT country_id FROM country WHERE country <> 'India')

The subquery returns multiple values (1, 2, 3, ..., 109), but country_id is a single value. You cannot check if one thing equals many things.

Solution: Use IN, ANY, or ALL operators instead of = for multi-row subqueries.

