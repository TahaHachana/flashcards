## Why Aliases Work In ORDER BY

Why can you use column aliases in ORDER BY but not in WHERE? Explain using processing order.

---

Processing order determines when aliases exist:

```
1. FROM table
2. WHERE conditions    ← Aliases don't exist yet
3. SELECT columns      ← Aliases created here
4. ORDER BY columns    ← Aliases exist now
```

Example:
```sql
SELECT price * quantity AS total
FROM orders
WHERE total > 100        -- ERROR! Alias doesn't exist
ORDER BY total;          -- WORKS! Alias exists
```

Why aliases work in ORDER BY:
- SELECT creates the alias
- ORDER BY processes after SELECT
- Therefore ORDER BY can see and use the alias

Why aliases don't work in WHERE:
- WHERE processes before SELECT
- Aliases haven't been created yet
- Therefore WHERE can't see them

Solution for WHERE: Repeat the calculation
```sql
WHERE price * quantity > 100
```

