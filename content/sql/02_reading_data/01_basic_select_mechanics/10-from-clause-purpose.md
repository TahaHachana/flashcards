## FROM Clause Purpose

What does the FROM clause do? Is it mandatory?

---

FROM specifies which table to query.

```sql
SELECT first_name, last_name
FROM customers;
```

Key points:
- FROM is mandatory (must specify data source)
- Table names may be case-sensitive (depends on database)
- Can query one table at a time (for now - JOINs come later)
- Processes first logically (before WHERE, SELECT, ORDER BY)

Without FROM, the database doesn't know where to get the data.

