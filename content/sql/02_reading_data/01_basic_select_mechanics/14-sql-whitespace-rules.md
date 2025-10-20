## SQL Whitespace Rules

How flexible is SQL with spacing and line breaks? What's the best practice?

---

SQL is very flexible with whitespace - spaces, tabs, and line breaks are mostly ignored.

These are equivalent:
```sql
SELECT first_name,last_name FROM customers WHERE age>18;

SELECT first_name, last_name
FROM customers
WHERE age > 18;
```

Best practices:
- Use whitespace for readability
- Put each major clause on its own line
- Indent sub-parts of clauses
- Space around operators (age > 18, not age>18)
- Be consistent within your codebase

The semicolon (;) marks the end of a statement - always include it.

