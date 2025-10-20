## Sorting Pattern Secondary Sort

Show the pattern for grouping by one column and sorting within groups by another.

---

Secondary sort pattern (group then sort within groups):

```sql
SELECT category, product_name, price
FROM products
ORDER BY category, price;
```

Result:
```
category     | product_name | price
-------------|--------------|-------
Electronics  | Radio        | 50
Electronics  | TV Basic     | 800
Electronics  | TV Pro       | 1200
Furniture    | Chair        | 200
Furniture    | Sofa         | 900
```

Products grouped by category, then sorted by price within each category.

Common variations:
```sql
-- Employees by department, then salary:
ORDER BY department, salary DESC

-- Orders by customer, then date:
ORDER BY customer_id, order_date

-- Products by category, highest rated first:
ORDER BY category, rating DESC, product_name
```

First column groups, subsequent columns sort within groups.

