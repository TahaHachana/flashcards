## Subqueries In HAVING Clause

How are subqueries used in the HAVING clause, and how does this differ from WHERE?

---

HAVING clause subqueries filter grouped/aggregated data based on comparisons to other aggregated results.

Difference from WHERE:
- WHERE filters individual rows before grouping
- HAVING filters groups after aggregation

Example - Find customers with more rentals than all North American customers:
SELECT customer_id, COUNT(*)
FROM rental
GROUP BY customer_id
HAVING COUNT(*) > ALL (SELECT COUNT(*) FROM ... WHERE country IN (...) GROUP BY ...);

The subquery returns aggregated values, and HAVING compares the current group's aggregate to them.

