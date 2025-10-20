## BETWEEN Operator Basics

What does the BETWEEN operator do? Is it inclusive or exclusive?

---

BETWEEN tests if a value falls within a range. It is INCLUSIVE (includes both boundary values).

```sql
WHERE age BETWEEN 18 AND 65
```

Equivalent to:
```sql
WHERE age >= 18 AND age <= 65
```

Examples:
```sql
-- Ages 18 through 65 (includes 18 and 65):
WHERE age BETWEEN 18 AND 65

-- Prices $10 to $100 (includes $10 and $100):
WHERE price BETWEEN 10.00 AND 100.00

-- Dates in January 2024 (includes Jan 1 and Jan 31):
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31'
```

Key point: BETWEEN is inclusive - both endpoints are included in the range.

