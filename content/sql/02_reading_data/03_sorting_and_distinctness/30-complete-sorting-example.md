## Complete Sorting Example

Explain how this query works:
```sql
SELECT category, product_name, price
FROM products
WHERE price > 0
ORDER BY category, price DESC;
```

---

Processing flow:

1. FROM products
   - Start with products table

2. WHERE price > 0
   - Filter to only products with price greater than 0
   - Excludes free items and possibly NULL prices

3. SELECT category, product_name, price
   - Choose these three columns from filtered rows

4. ORDER BY category, price DESC
   - First, group by category (alphabetically)
   - Within each category, sort by price (highest first)

Example result:
```
category     | product_name | price
-------------|--------------|-------
Electronics  | TV Pro       | 1200
Electronics  | TV Basic     | 800
Electronics  | Radio        | 50
Furniture    | Sofa         | 900
Furniture    | Chair        | 200
```

Products grouped by category, expensive items first within each category.

