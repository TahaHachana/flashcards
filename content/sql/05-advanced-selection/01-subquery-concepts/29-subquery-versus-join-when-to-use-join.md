## Subquery Versus JOIN When To Use JOIN

When should you use a JOIN instead of a subquery?

---

Use JOINs when:

1. You need columns from multiple tables in the result set
   - SELECT c.name, o.total FROM customers c JOIN orders o ...

2. Performance is critical and the subquery would run once per row
   - Correlated subqueries in SELECT clause are often inefficient

3. The relationship is straightforward
   - Simple foreign key relationships

4. You're accessing the same table multiple times via subqueries
   - Better to JOIN once than subquery multiple times

Bad (inefficient - 3 subqueries):
SELECT (SELECT first_name FROM customer WHERE id = p.customer_id),
       (SELECT last_name FROM customer WHERE id = p.customer_id), ...

Good (efficient - 1 JOIN):
SELECT c.first_name, c.last_name, ... FROM payment p JOIN customer c ON ...

