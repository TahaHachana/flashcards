## NOT LIKE

How does NOT LIKE work? Give practical examples.

---

NOT LIKE excludes rows matching the pattern.

```sql
-- Exclude names starting with 'A':
WHERE name NOT LIKE 'A%'

-- Exclude example.com emails:
WHERE email NOT LIKE '%@example.com'

-- Exclude codes starting with 'X':
WHERE code NOT LIKE 'X%'

-- Exclude anything containing 'test':
WHERE description NOT LIKE '%test%'
```

Useful for:
- Filtering out test data
- Excluding specific patterns
- Finding anomalies
- Data cleanup

Example use case:
```sql
-- Find non-example email addresses:
WHERE email NOT LIKE '%@example.com'
AND email NOT LIKE '%@test.com'
```

