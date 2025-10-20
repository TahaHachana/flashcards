## Multiple Clauses Required Order

What is the required order for writing SELECT statement clauses? Can you reorder them?

---

Required written order (cannot change):
```sql
SELECT columns
FROM table
WHERE conditions
ORDER BY columns
```

This order is mandatory - you'll get a syntax error if you write them differently.

Example of WRONG order:
```sql
FROM customers        -- ERROR!
WHERE age > 18
SELECT name
```

Why this order?
SQL syntax rules require it, even though the logical execution order is different (FROM → WHERE → SELECT → ORDER BY).

Remember: Written order ≠ Execution order, but written order is fixed.

