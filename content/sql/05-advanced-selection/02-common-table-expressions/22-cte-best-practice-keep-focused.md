## CTE Best Practice Keep Focused

What does "keep CTEs focused" mean, and why is it important?

---

Principle: Each CTE should do ONE logical thing.

Bad (CTE doing too much):
WITH everything AS (
  SELECT c.name, o.total, o.date, p.category,
         CASE WHEN ... END as tier,
         ROW_NUMBER() OVER (...) as rank
  FROM customers c
  JOIN orders o ON ... JOIN products p ON ...
  WHERE complex conditions
  GROUP BY ... HAVING ...
)
SELECT * FROM everything WHERE ...;
-- What is this CTE's purpose? Unclear!

Good (separate concerns):
WITH customer_orders AS (
  -- Get orders from 2024
  SELECT customer_id, order_id, order_date, total
  FROM orders
  WHERE order_date >= '2024-01-01'
),
order_categories AS (
  -- Add product category to each order
  SELECT co.order_id, p.category
  FROM customer_orders co
  JOIN products p ON ...
),
category_totals AS (
  -- Calculate spending per customer per category
  SELECT customer_id, category, SUM(total) as total
  FROM customer_orders co
  JOIN order_categories oc ON co.order_id = oc.order_id
  GROUP BY customer_id, category
)
SELECT * FROM category_totals WHERE total > 1000;

Benefits of focused CTEs:
- Each CTE has clear, single purpose
- Easy to understand what each step does
- Easy to test each step independently
- Easy to modify one step without affecting others
- Easy to reuse individual steps if needed

