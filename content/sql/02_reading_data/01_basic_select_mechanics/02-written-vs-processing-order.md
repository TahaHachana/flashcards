## Written Order vs Processing Order

What is the difference between the written order and the logical processing order of SELECT statement clauses?

---

Written order (how you type it):
```sql
SELECT columns
FROM table
WHERE conditions
ORDER BY columns
```

Logical processing order (how database executes):
```
1. FROM table
2. WHERE conditions
3. SELECT columns
4. ORDER BY columns
```

Why it matters: Understanding processing order explains why aliases work in ORDER BY but not WHERE, and why you can filter on columns you don't select.

