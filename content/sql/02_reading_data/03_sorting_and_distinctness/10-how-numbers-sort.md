## How Numbers Sort

How do numbers sort in ORDER BY? What's the difference between numeric and text sorting?

---

Numbers stored as numeric type:
- Ascending: -100, -1, 0, 1, 2, 10, 100 (by magnitude)
- Descending: 100, 10, 2, 1, 0, -1, -100

Numbers stored as text type:
- Ascending: '1', '10', '100', '2', '20' (alphabetically!)
- Descending: '20', '2', '100', '10', '1'

Problem with text:
```sql
-- If price is TEXT:
ORDER BY price
-- Result: '10', '100', '2', '5'  -- WRONG!

-- If price is INT:
ORDER BY price
-- Result: 2, 5, 10, 100  -- CORRECT!
```

This is why using correct data types matters!

Text compares character-by-character: '1' < '2', but '10' < '2' alphabetically.

