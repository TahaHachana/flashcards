## Subquery Composition Of Logic

How do subqueries enable "composition of logic" in SQL? Provide an example.

---

Subqueries let you nest operations that would otherwise require multiple separate queries, composing complex logic into a single statement.

Without subqueries (2 queries):
-- Query 1: Get the average
SELECT AVG(amount) FROM payment; -- Returns: 4.20

-- Query 2: Use that value manually
SELECT customer_id, amount FROM payment WHERE amount > 4.20;

With subquery (1 query):
SELECT customer_id, amount 
FROM payment 
WHERE amount > (SELECT AVG(amount) FROM payment);

The subquery composes the calculation into the filtering logic. You can nest these arbitrarily deep:

SELECT ... WHERE x > (SELECT AVG(y) FROM (SELECT ... FROM ... WHERE ...) subquery);

Composition enables: Calculate → Filter → Aggregate → Filter again, all in one logical flow.

