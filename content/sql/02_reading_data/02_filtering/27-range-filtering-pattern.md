## Range Filtering Pattern

Show different ways to filter values within a range.

---

Range filtering options:

1. Using BETWEEN (inclusive):
```sql
WHERE age BETWEEN 18 AND 65
WHERE price BETWEEN 10 AND 100
```

2. Using AND with comparison operators:
```sql
WHERE age >= 18 AND age <= 65
WHERE price >= 10 AND price <= 100
```

3. Exclusive ranges:
```sql
-- Exclude boundaries:
WHERE age > 18 AND age < 65
```

4. One-sided ranges:
```sql
-- Just minimum:
WHERE price >= 50

-- Just maximum:
WHERE age < 18
```

5. Multiple ranges:
```sql
-- Teenagers OR seniors:
WHERE (age BETWEEN 13 AND 19) 
   OR (age >= 65)
```

BETWEEN is cleaner for inclusive ranges; use operators for exclusive or complex ranges.

