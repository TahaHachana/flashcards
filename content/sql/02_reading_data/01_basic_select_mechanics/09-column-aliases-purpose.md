## Column Aliases Purpose

What are column aliases? Why use them?

---

Aliases give names to calculated columns or rename existing columns.

Syntax:
```sql
SELECT price * quantity AS total FROM orders;
SELECT height / 2.54 AS height_in_inches FROM customers;
```

Why use them:
1. Make results clearer (column labeled "total" not "price * quantity")
2. Required for calculations in ORDER BY
3. Make query more readable
4. Can rename confusing column names

Notes:
- AS keyword is optional but recommended
- Alias names should be descriptive
- Can't start with a number
- Use quotes if name has spaces: AS "Total Price"

