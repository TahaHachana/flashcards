## NULL Cannot Use Equals

Why doesn't `WHERE age = NULL` work? What's the correct way to check for NULL?

---

`WHERE age = NULL` never matches anything, even rows with NULL!

Why: NULL means "unknown". Is an unknown value equal to another unknown? We don't know, so the result is NULL (not TRUE).

Correct way:
```sql
-- Find NULL values:
WHERE phone IS NULL

-- Find non-NULL values:
WHERE phone IS NOT NULL
```

Wrong:
```sql
WHERE age = NULL     -- Never matches
WHERE age <> NULL    -- Never matches
```

Right:
```sql
WHERE age IS NULL        -- Matches NULL
WHERE age IS NOT NULL    -- Matches non-NULL
```

Remember: Use IS NULL / IS NOT NULL, never = NULL or <> NULL.

