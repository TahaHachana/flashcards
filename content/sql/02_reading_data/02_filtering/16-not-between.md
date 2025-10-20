## NOT BETWEEN

How does NOT BETWEEN work? What is it equivalent to?

---

NOT BETWEEN excludes values within the range.

```sql
WHERE age NOT BETWEEN 18 AND 65
```

Equivalent to:
```sql
WHERE age < 18 OR age > 65
```

Includes values OUTSIDE the range (both below and above).

Examples:
```sql
-- Ages under 18 OR over 65:
WHERE age NOT BETWEEN 18 AND 65

-- Prices NOT in the $10-$100 range:
WHERE price NOT BETWEEN 10 AND 100

-- Dates NOT in January:
WHERE order_date NOT BETWEEN '2024-01-01' AND '2024-01-31'
```

Note: It's OR logic (< lower OR > higher), not AND.

