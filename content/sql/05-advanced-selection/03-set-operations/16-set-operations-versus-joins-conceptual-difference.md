## Set Operations Versus JOINs Conceptual Difference

What is the fundamental conceptual difference between set operations and JOINs?

---

JOINs:
- Combine tables HORIZONTALLY (adding columns)
- Match rows based on relationships (foreign keys)
- Result: Wider table (more columns)
- Use case: "I need data from multiple related tables in the same row"

Set Operations:
- Combine result sets VERTICALLY (adding rows)
- Stack rows from different sources
- Result: Taller table (more rows, same columns)
- Use case: "I need rows from multiple similar sources in one list"

JOIN example - Customer orders with product details:
SELECT c.first_name, c.last_name, o.order_date, o.total
FROM customer c
INNER JOIN orders o ON c.customer_id = o.customer_id;
-- Each row has customer columns + order columns (wider)

Set operation example - All people from multiple tables:
SELECT first_name, last_name, 'Customer' AS type FROM customer
UNION ALL
SELECT first_name, last_name, 'Employee' AS type FROM employee;
-- All rows from both tables stacked together (taller)

Mental model: JOINs = side by side; Set operations = stacked on top.

