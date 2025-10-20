## Excluding Values Pattern

Show different ways to exclude specific values in WHERE clauses.

---

Multiple ways to exclude values:

1. Not equal:
```sql
WHERE status <> 'Cancelled'
WHERE status != 'Cancelled'  -- Same thing
```

2. NOT IN:
```sql
WHERE category NOT IN ('Discontinued', 'Out of Stock')
```

3. NOT LIKE:
```sql
WHERE email NOT LIKE '%@test.com'
```

4. NOT BETWEEN:
```sql
WHERE age NOT BETWEEN 0 AND 17  -- Exclude minors
```

5. Combining:
```sql
WHERE status <> 'Cancelled'
  AND category NOT IN ('Test', 'Sample')
  AND name NOT LIKE '%DELETE%'
```

Choose based on what you're excluding:
- Single value: use <>
- Multiple values: use NOT IN
- Patterns: use NOT LIKE
- Ranges: use NOT BETWEEN

