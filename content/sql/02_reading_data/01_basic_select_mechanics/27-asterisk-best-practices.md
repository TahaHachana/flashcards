## Asterisk Best Practices

When is it acceptable to use SELECT * and when should you avoid it?

---

Acceptable uses:
- Ad-hoc queries and exploration
- Learning/testing with new tables
- Quick checks during development
- When you genuinely need all columns

Avoid in production:
- Application code
- Stored procedures
- Reports
- Any code that will be maintained

Why avoid:
```sql
-- Today: customers has 5 columns
SELECT * FROM customers;

-- Tomorrow: customers adds 6th column
-- Your code might break or behave unexpectedly
```

Best practice:
```sql
-- Instead of:
SELECT * FROM customers;

-- Write:
SELECT id, name, email, phone FROM customers;
```

Explicit is better than implicit in production code.

