## Subquery Versus JOIN When To Use Subquery

When should you use a subquery instead of a JOIN?

---

Use subqueries when:

1. You need a calculated value for filtering or comparison
   - WHERE total > (SELECT AVG(total) FROM ...)

2. The relationship is complex and a subquery makes logic clearer
   - Nested aggregations or multi-step calculations

3. You're checking for existence/non-existence
   - WHERE EXISTS / WHERE NOT EXISTS

4. You need to aggregate first, then join the result
   - FROM (SELECT customer_id, SUM(amount) FROM payment GROUP BY ...) totals

5. The subquery result is used only for filtering, not in output
   - You don't need columns from both tables in results

