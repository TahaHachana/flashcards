## Why Alias Works in ORDER BY Not WHERE

Why can you use column aliases in ORDER BY but not in WHERE? Explain using processing order.

---

Processing order determines when aliases exist:

```
1. FROM table
2. WHERE conditions    ← Alias doesn't exist yet
3. SELECT columns      ← Alias created here
4. ORDER BY columns    ← Alias now exists
```

Example:
```sql
SELECT price * quantity AS total
FROM orders
WHERE total > 100        -- ERROR! Alias doesn't exist yet
ORDER BY total;          -- WORKS! Alias exists now
```

Fix for WHERE:
```sql
WHERE price * quantity > 100  -- Repeat the calculation
```

ORDER BY can use aliases because SELECT creates them before ORDER BY executes.

