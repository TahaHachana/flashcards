## Finding Missing Data Pattern

How do you find rows with missing (NULL) data? Give examples.

---

Use IS NULL to find missing data:

```sql
-- Customers without email:
WHERE email IS NULL

-- Products without descriptions:
WHERE description IS NULL

-- Orders not yet shipped:
WHERE ship_date IS NULL

-- Either NULL or empty string:
WHERE phone IS NULL OR phone = ''

-- Multiple missing fields:
WHERE email IS NULL AND phone IS NULL
```

Finding non-missing data:
```sql
-- Customers WITH email:
WHERE email IS NOT NULL

-- Products with prices:
WHERE price IS NOT NULL

-- Required fields filled:
WHERE name IS NOT NULL 
  AND email IS NOT NULL
  AND phone IS NOT NULL
```

Common in data quality checks and validation queries.

