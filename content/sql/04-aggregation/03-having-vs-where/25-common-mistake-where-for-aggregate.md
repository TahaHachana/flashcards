## Common Mistake WHERE for Aggregate

What's wrong with this query and how do you fix it? `SELECT state, COUNT(*) FROM customers WHERE COUNT(*) > 100 GROUP BY state;`

---

Wrong: WHERE COUNT(*) > 100 tries to use an aggregate in WHERE, which causes an error. Fix: Move it to HAVING. Correct query: SELECT state, COUNT(*) FROM customers GROUP BY state HAVING COUNT(*) > 100. This groups by state first, calculates counts, then filters to states with 100+ customers.

