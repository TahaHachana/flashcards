## Result Set vs Stored Table

What's the difference between a result set and a stored table?

---

Stored table:
- Permanently stored in database
- Data persists between queries
- Can be modified (INSERT, UPDATE, DELETE)
- Has defined structure (schema)
- Physical storage on disk

Result set:
- Temporary, exists only during query
- Disappears after query completes
- Cannot be modified (it's output)
- Structure defined by SELECT clause
- Exists only in memory

Key insight:
When you run `SELECT * FROM customers`, the customers table is stored, but the result you see is a temporary result set.

Both are tables (rows + columns), but one is persistent, one is temporary.

