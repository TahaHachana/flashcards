## Complex Filter Example

Explain how this complex WHERE clause works:
```sql
WHERE (category = 'Electronics' OR category = 'Computers')
  AND price BETWEEN 100 AND 1000
  AND product_name LIKE '%Pro%'
  AND discontinued IS NOT TRUE
```

---

This finds products matching ALL of these:

1. `(category = 'Electronics' OR category = 'Computers')`
   - Must be in either category

2. `AND price BETWEEN 100 AND 1000`
   - Must cost $100-$1000

3. `AND product_name LIKE '%Pro%'`
   - Must have "Pro" in the name

4. `AND discontinued IS NOT TRUE`
   - Must not be discontinued

Processing:
- Each condition evaluates to TRUE/FALSE/NULL for every row
- All conditions connected with AND must be TRUE
- Only rows where final result is TRUE are included

Example matching row:
- category: 'Electronics'
- price: 599
- product_name: 'MacBook Pro'
- discontinued: FALSE

