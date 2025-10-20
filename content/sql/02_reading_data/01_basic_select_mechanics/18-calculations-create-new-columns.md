## Calculations Create New Columns

When you write `SELECT price * 2 FROM products`, where does this calculated column exist?

---

The calculated column exists ONLY in the result set (temporary table), NOT in the stored table.

```sql
SELECT price, price * 2 AS doubled
FROM products;
```

Result set has two columns:
- price (from table)
- doubled (calculated, temporary)

Key points:
- Calculation happens during query execution
- Result is not stored anywhere
- Original table is unchanged
- Each time you run the query, it recalculates
- Useful for transforming data without modifying storage

This is the difference between result sets and stored tables.

