## CTE Best Practice Test Independently

How should you test CTEs during query development, and why is this approach valuable?

---

Approach: Test each CTE independently before building on it.

Development workflow:

Step 1: Build and test first CTE
WITH customer_totals AS (
  SELECT customer_id, SUM(amount) as total
  FROM payment
  GROUP BY customer_id
)
SELECT * FROM customer_totals LIMIT 10;
-- Verify: Does this return expected data?

Step 2: Add second CTE and test
WITH 
  customer_totals AS (...),
  high_value_customers AS (
    SELECT customer_id FROM customer_totals WHERE total > 100
  )
SELECT * FROM high_value_customers LIMIT 10;
-- Verify: Are these the right high-value customers?

Step 3: Add main query
WITH 
  customer_totals AS (...),
  high_value_customers AS (...)
SELECT c.first_name, c.last_name, hvc.customer_id
FROM high_value_customers hvc
JOIN customer c ON hvc.customer_id = c.customer_id;

Why this is valuable:
- Catches errors early in specific CTEs
- Avoids debugging complex nested logic
- Confirms each step produces expected results
- Documents expected intermediate results
- Makes development iterative and controlled

Debugging: If final query is wrong, test each CTE independently to find which step has the problem.

