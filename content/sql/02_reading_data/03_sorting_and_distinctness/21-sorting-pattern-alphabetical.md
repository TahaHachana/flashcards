## Common Sorting Pattern Alphabetical

Show the common pattern for alphabetical listings by name.

---

Alphabetical by name pattern:

```sql
SELECT first_name, last_name
FROM customers
ORDER BY last_name, first_name;
```

Why this order:
1. Sort by last_name primarily
2. Use first_name as tiebreaker

Common variations:
```sql
-- Products alphabetically:
SELECT product_name, price
FROM products
ORDER BY product_name;

-- Employees by department, then name:
SELECT department, last_name, first_name
FROM employees
ORDER BY department, last_name, first_name;

-- Categories alphabetically:
SELECT DISTINCT category
FROM products
ORDER BY category;
```

Last name first is convention for people; single name for other entities.

