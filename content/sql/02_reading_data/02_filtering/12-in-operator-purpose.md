## IN Operator Purpose

What does the IN operator do? How is it better than multiple OR conditions?

---

IN tests whether a value matches any value in a list.

Instead of:
```sql
WHERE country = 'USA' OR country = 'Canada' OR country = 'Mexico'
```

Use IN:
```sql
WHERE country IN ('USA', 'Canada', 'Mexico')
```

Much cleaner!

Examples:
```sql
-- Specific states:
WHERE state IN ('CA', 'NY', 'TX')

-- Specific IDs:
WHERE product_id IN (101, 102, 103, 104)

-- Dates:
WHERE order_date IN ('2024-01-15', '2024-02-20')
```

Benefits:
- More readable
- Easier to maintain (add/remove values)
- Shorter syntax
- Clearer intent

