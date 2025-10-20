## Ascending Order Default

What is the default sort direction in ORDER BY? What does ascending mean for different data types?

---

Default is ascending (ASC is optional):

```sql
ORDER BY last_name
ORDER BY last_name ASC  -- Same thing
```

Ascending means:
- Numbers: Smallest to largest (1, 2, 3, 10, 100)
- Text: Alphabetical (A, B, C... Z)
- Dates: Oldest to newest (2020, 2021, 2024)

Examples:
```sql
-- Cheapest products first:
ORDER BY price

-- Alphabetical by name:
ORDER BY last_name

-- Oldest orders first:
ORDER BY order_date
```

ASC keyword is redundant since it's default.

