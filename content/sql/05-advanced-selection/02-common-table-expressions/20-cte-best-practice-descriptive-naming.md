## CTE Best Practice Descriptive Naming

Why are descriptive CTE names important, and what makes a good CTE name?

---

Importance: CTE names are documentation - they explain what the intermediate result contains.

Bad (cryptic):
WITH t1 AS (...), t2 AS (...), t3 AS (...)
SELECT * FROM t3;
-- What do t1, t2, t3 represent? Unclear!

Good (descriptive):
WITH active_customers AS (...),
     customer_lifetime_value AS (...),
     high_value_segments AS (...)
SELECT * FROM high_value_segments;
-- Clear: Each step explains itself

Guidelines for good names:

1. Use nouns or noun phrases (CTEs are things):
   - ✓ monthly_revenue
   - ✗ calculate_revenue

2. Describe the data, not the operation:
   - ✓ customers_with_recent_orders
   - ✗ filter_customers

3. Be specific enough to differentiate:
   - ✓ customer_payment_totals, customer_rental_counts
   - ✗ customer_data, customer_info

4. Follow project naming conventions:
   - snake_case or camelCase consistently
   - Plural for sets: active_customers, not active_customer

Think: "If I read this query in 6 months, will the CTE name tell me what it contains?"

