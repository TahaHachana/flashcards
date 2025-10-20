## SELECT Processes After WHERE

Why does SELECT process after WHERE? What's the practical impact?

---

Processing order: FROM → WHERE → SELECT

Why:
1. FROM identifies the table
2. WHERE filters rows from that table
3. SELECT chooses columns from filtered rows

Practical impact:

Can do this:
```sql
SELECT name, age
FROM customers
WHERE registration_date > '2024-01-01';
```

Can't do this:
```sql
SELECT name, age
FROM customers
WHERE name = 'John';  -- Works fine
WHERE total > 100;    -- ERROR if total is calculated in SELECT
```

WHERE sees original table columns, not SELECT calculations/aliases.

