## Filter On Unselected Columns

Can you filter on columns that aren't in your SELECT clause? Give a practical example.

---

Yes! WHERE can filter on any column in the table, even columns not in SELECT.

Example:
```sql
SELECT product_name, price
FROM products
WHERE category = 'Electronics'
  AND stock_quantity > 0
  AND discontinued = FALSE;
```

Result shows product_name and price, but filters using:
- category (not shown)
- stock_quantity (not shown)
- discontinued (not shown)

Why this works:
Processing order:
1. FROM products (all columns available)
2. WHERE filters using any columns
3. SELECT chooses which columns to show

Use case: "Show me product names and prices for in-stock, non-discontinued electronics"

You don't need to show the filtering columns - you just need the data that meets those criteria.

