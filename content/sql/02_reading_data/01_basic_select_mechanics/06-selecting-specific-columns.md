## Selecting Specific Columns

How do you select specific columns? What are the benefits over SELECT *?

---

Syntax:
```sql
SELECT first_name, last_name, email FROM customers;
```

Benefits:
1. Explicitly states what data you need
2. More efficient (only retrieves needed columns)
3. More maintainable (clear what the query does)
4. Doesn't break if table adds new columns
5. Better performance

Key points:
- Columns separated by commas
- Can select in any order (doesn't have to match table order)
- Column names are case-insensitive

