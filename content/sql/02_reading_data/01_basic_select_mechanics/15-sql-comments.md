## SQL Comments

What are the two ways to write comments in SQL? When should you use them?

---

Two comment styles:

Single-line:
```sql
-- This is a comment
SELECT * FROM customers; -- This is also a comment
```

Multi-line:
```sql
/*
This is a comment
spanning multiple lines
*/
SELECT * FROM customers;
```

Use comments to:
- Explain complex logic
- Document business rules
- Provide context for future maintainers
- Temporarily disable code during testing
- Add authorship/date information

