## DISTINCT Problematic With ORDER BY

Why might `SELECT DISTINCT country ORDER BY registration_date` be problematic?

---

Problem: You're getting distinct countries, but sorting by registration_date.

```sql
SELECT DISTINCT country
FROM customers
ORDER BY registration_date;
```

Which registration_date should be used?
- USA appears 100 times with 100 different registration dates
- Which date determines where USA appears in sorted results?
- Ambiguous and may cause errors

Different databases handle this differently:
- Some fail with an error
- Some pick arbitrary date
- Result is unpredictable

Solution: Only sort by columns in your SELECT when using DISTINCT:

```sql
-- Safe:
SELECT DISTINCT country
FROM customers
ORDER BY country;
```

Rule: With DISTINCT, ORDER BY columns should be in the SELECT clause.

