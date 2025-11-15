## Subquery Shapes Determine Operators

How does the "shape" of a subquery's result set determine what operators you can use with it?

---

The shape (rows × columns) determines valid operators:

1. Scalar (1 row × 1 column) - Single value:
   - Use: =, <>, <, >, <=, >=
   - Example: WHERE customer_id = (SELECT MAX(customer_id) FROM customer)

2. Multiple rows × 1 column - List of values:
   - Use: IN, NOT IN, ALL, ANY, EXISTS, NOT EXISTS
   - Example: WHERE city IN (SELECT city FROM ...)

3. Multiple rows × Multiple columns - Table:
   - Use: IN with column list
   - Example: WHERE (actor_id, film_id) IN (SELECT actor_id, film_id FROM ...)

Mismatch errors:
- Using = with multi-row subquery → Error: "Subquery returns more than 1 row"
- Using IN without column list for multicolumn → Syntax error

Mental model: Match the operator to the result shape.

