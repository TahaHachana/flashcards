## WHERE Comes Before SELECT

Why does WHERE process before SELECT? What does this enable you to do?

---

Processing order: FROM → WHERE → SELECT

Why:
- WHERE filters on the full table (all columns available)
- SELECT then narrows to specific columns

This enables:
1. Filtering on columns you don't select
```sql
SELECT name FROM customers WHERE registration_date > '2024-01-01';
```

2. WHERE sees original table columns, not SELECT calculations
```sql
-- This works:
WHERE age >= 18

-- This doesn't work:
SELECT age * 2 AS doubled
WHERE doubled >= 36  -- ERROR! doubled doesn't exist yet
```

WHERE operates on the source table, SELECT operates on filtered results.

