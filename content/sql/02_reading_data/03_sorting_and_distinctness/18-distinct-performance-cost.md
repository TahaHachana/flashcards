## DISTINCT Performance Cost

Why can DISTINCT be expensive? When should you use it and when should you avoid it?

---

DISTINCT is expensive because it must:
1. Retrieve all rows
2. Sort or hash them to find duplicates
3. Remove duplicates
4. Return remaining rows

When to use:
- When you genuinely need unique values
- For dropdowns/lists of options
- When duplicates would confuse users
- For counting unique values

When to avoid:
- As a "quick fix" for poorly designed queries
- When data is already unique
- On very large result sets without good reason
- As a band-aid for bad joins creating duplicates

Bad use:
```sql
-- Using DISTINCT to hide a join problem:
SELECT DISTINCT customer_name FROM orders JOIN customers ...
-- Better: Fix the join logic
```

Good use:
```sql
-- Getting unique categories for a dropdown:
SELECT DISTINCT category FROM products ORDER BY category;
```

