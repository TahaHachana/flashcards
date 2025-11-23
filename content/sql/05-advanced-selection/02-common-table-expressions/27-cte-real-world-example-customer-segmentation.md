## CTE Real World Example Customer Segmentation

Walk through how CTEs improve a real-world customer segmentation query.

---

Task: Classify customers into tiers and analyze each tier.

Without CTEs (hard to read):
SELECT tier, COUNT(*), AVG(total_spent)
FROM (
  SELECT customer_id,
         CASE WHEN (SELECT SUM(amount) FROM payment WHERE customer_id = c.customer_id) >= 150 THEN 'Premium'
              WHEN (SELECT SUM(amount) FROM payment WHERE customer_id = c.customer_id) >= 75 THEN 'Standard'
              ELSE 'Basic' END as tier,
         (SELECT SUM(amount) FROM payment WHERE customer_id = c.customer_id) as total_spent
  FROM customer c
) subquery
GROUP BY tier;

With CTEs (clear and logical):
WITH 
  customer_totals AS (
    -- Step 1: Calculate total spending per customer
    SELECT customer_id, SUM(amount) as total_spent
    FROM payment
    GROUP BY customer_id
  ),
  customer_tiers AS (
    -- Step 2: Classify customers into tiers
    SELECT customer_id, total_spent,
           CASE 
             WHEN total_spent >= 150 THEN 'Premium'
             WHEN total_spent >= 75 THEN 'Standard'
             ELSE 'Basic'
           END as tier
    FROM customer_totals
  )
-- Step 3: Analyze each tier
SELECT tier, 
       COUNT(*) as customer_count,
       AVG(total_spent) as avg_spent
FROM customer_tiers
GROUP BY tier;

Improvements:
- Each step has a name explaining its purpose
- Logic flows naturally top-to-bottom
- Can test customer_totals independently
- No repeated calculations
- Easy to modify tier definitions

