## Common Sorting Pattern Top N

Show the common pattern for getting top N results (most expensive, highest rated, etc.).

---

Top N pattern requires ORDER BY + LIMIT/TOP:

```sql
-- Most expensive products (top 10):
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 10;
```

Key elements:
1. ORDER BY with DESC for "top"
2. LIMIT to restrict count (LIMIT 10, TOP 10, etc.)

Common variations:
```sql
-- Highest rated:
ORDER BY rating DESC LIMIT 5

-- Best sellers:
ORDER BY units_sold DESC LIMIT 20

-- Top earners:
ORDER BY salary DESC LIMIT 10

-- Lowest prices:
ORDER BY price ASC LIMIT 10
```

Without ORDER BY, LIMIT gives random rows!

Syntax varies: LIMIT (MySQL/PostgreSQL), TOP (SQL Server)

