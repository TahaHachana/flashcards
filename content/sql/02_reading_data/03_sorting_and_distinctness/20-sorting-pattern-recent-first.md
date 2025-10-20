## Common Sorting Pattern Recent First

Show the common pattern for displaying most recent records first.

---

Most recent first pattern:

```sql
SELECT *
FROM orders
ORDER BY order_date DESC;
```

DESC because you want newest (largest date values) first.

Common variations:
```sql
-- Most recent 10 orders:
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 10;

-- Recent activity:
SELECT *
FROM user_activity
ORDER BY timestamp DESC;

-- Latest updates:
SELECT *
FROM products
ORDER BY updated_at DESC;

-- Newest customers:
SELECT *
FROM customers
ORDER BY registration_date DESC;
```

DESC is key - puts newest dates at the top.

