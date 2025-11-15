## Subqueries Extend SQL Toolkit

What capabilities do subqueries add to your SQL toolkit beyond basic SELECT/FROM/WHERE?

---

Subqueries extend SQL to:

1. Filter on calculated values (WHERE/HAVING with subqueries)
   - WHERE amount > (SELECT AVG(amount) FROM ...)

2. Generate values dynamically (SELECT clause)
   - SELECT name, (SELECT COUNT(*) FROM orders WHERE ...) order_count

3. Create virtual tables (FROM clause)
   - FROM (SELECT customer_id, SUM(amount) FROM ...) totals

4. Look up values during INSERT/UPDATE/DELETE
   - INSERT INTO table VALUES ((SELECT id FROM ...), ...)

5. Check existence/non-existence efficiently
   - WHERE EXISTS / WHERE NOT EXISTS

6. Implement complex filtering logic without procedural code
   - All in declarative SQL

Core insight: Subqueries transform SQL from "query this table" to "query anything I can express as a query," enabling query-driven programming.

