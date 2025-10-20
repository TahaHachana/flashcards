## Everything Is a Table Concept

Why is the concept "everything is a table" important in SQL?

---

Understanding that result sets are tables helps with advanced SQL.

Key points:
1. Tables in the database → contain stored data
2. Result sets from queries → temporary tables
3. Both have rows and columns
4. Both can be operated on with SQL

Why this matters:
- Many SQL operations work on tables
- You can nest queries (subqueries) because they return tables
- You can JOIN result sets like you JOIN tables
- Consistent mental model throughout SQL

Example:
```sql
SELECT * FROM customers;  -- Returns a table (result set)
```

This result set IS a table, just temporary.

