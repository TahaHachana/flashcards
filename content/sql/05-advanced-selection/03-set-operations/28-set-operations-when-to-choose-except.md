## Set Operations When To Choose EXCEPT

When should you use EXCEPT, and what questions does it answer?

---

Use EXCEPT when you need to answer: "What's in A but NOT in B?"

Ideal use cases:

1. Finding missing data
   - Customers who haven't made purchases
   - Products with no sales
   - Required records that are missing

2. Data quality checks
   - Records that should exist but don't
   - Orphaned records (references to non-existent data)
   - Gaps in sequences

3. Finding exclusive membership
   - Customers who only bought from category A, not B
   - Users who took action X but not action Y

4. Comparative analysis
   - What changed between yesterday and today?
   - New items in current data vs historical

Example scenarios:

Missing data: "Customers with no purchases"
SELECT customer_id FROM customer
EXCEPT
SELECT customer_id FROM purchases;

Data quality: "Products referenced but not in catalog"
SELECT DISTINCT product_id FROM order_items
EXCEPT
SELECT product_id FROM products;

Change tracking: "New users this week"
SELECT user_id FROM users_current
EXCEPT
SELECT user_id FROM users_last_week;

When alternative is better: LEFT JOIN with NULL check gives you full row details; EXCEPT gives you just the ID.

