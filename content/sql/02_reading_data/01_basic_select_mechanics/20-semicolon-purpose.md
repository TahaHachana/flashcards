## Semicolon Purpose

What does the semicolon do in SQL? When is it required?

---

The semicolon (;) marks the end of a SQL statement.

Required when:
- Executing multiple statements together
- Standard practice even for single statements
- Some tools require it

Example:
```sql
SELECT * FROM customers;
SELECT * FROM products;
```

Without semicolons, the database wouldn't know where one statement ends and another begins.

Best practice: Always include semicolon, even for single statements. Makes code consistent and prevents errors when adding more statements.

Exception: Some interactive tools make it optional for single statements.

