## CTE Best Practice Add Comments

When and how should you add comments to CTEs?

---

When to add comments:
- Complex filtering or transformation logic
- Business rule implementations
- Calculations that aren't self-evident
- Exclusions or special cases
- Any logic that might be questioned

How to add effective comments:

1. Explain WHY, not WHAT:
-- Bad: "Select revenue by month"
-- Good: "Calculate monthly revenue for trend analysis"

2. Document exclusions and special cases:
WITH monthly_revenue AS (
  -- Excludes refunded orders and cancelled subscriptions
  -- per accounting policy doc #123
  SELECT 
    DATE_TRUNC('month', order_date) as month,
    SUM(amount) as revenue
  FROM orders
  WHERE status NOT IN ('refunded', 'cancelled')
  GROUP BY DATE_TRUNC('month', order_date)
)

3. Document business logic:
WITH high_value_customers AS (
  -- "High value" defined as >$1000 spend in last 90 days
  -- OR >20 orders lifetime (per marketing team definition)
  SELECT customer_id
  FROM ...
)

4. Note dependencies or assumptions:
-- Assumes payment.status is always populated (validated in ETL)

Avoid: Obvious comments like "this selects customers" for "SELECT * FROM customer"

