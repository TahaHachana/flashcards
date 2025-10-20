## When Database Decides How

What does it mean that "the database decides HOW to retrieve data"? Why does this matter?

---

When you write:
```sql
SELECT name FROM customers WHERE age >= 18;
```

You specify WHAT (names of adults), not HOW:
- Which index to use?
- Read full table or use index?
- In what order to process data?
- How much memory to allocate?

The database's query optimizer decides the HOW based on:
- Table size
- Available indexes
- Data distribution
- System resources

Why this matters:
1. Same query can execute differently over time (as data grows)
2. Database can optimize automatically
3. You don't need to know internal algorithms
4. Adding indexes can speed up queries without changing SQL

This is the power of declarative programming.

