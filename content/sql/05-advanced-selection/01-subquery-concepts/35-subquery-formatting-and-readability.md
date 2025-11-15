## Subquery Formatting And Readability

What are best practices for formatting subqueries to maintain readability?

---

Best practices:

1. Use consistent indentation to show nesting:
SELECT first_name, last_name
FROM customer c
WHERE EXISTS 
  (SELECT 1 
   FROM rental r 
   WHERE r.customer_id = c.customer_id 
     AND rental_date < '2005-05-25');

2. Name subqueries in FROM clause with meaningful aliases:
FROM (SELECT customer_id, SUM(amount) total FROM payment GROUP BY customer_id) customer_totals
     -- Descriptive name ↑

3. Document complex subqueries with comments:
-- Find customers who outspent at least one South American country
HAVING SUM(amount) > ANY (SELECT SUM(amount) FROM ... GROUP BY country);

4. Break complex queries into CTEs when appropriate
-- Common Table Expressions coming in section 5.2

Principle: Code is read more often than written. Make your intent clear.

