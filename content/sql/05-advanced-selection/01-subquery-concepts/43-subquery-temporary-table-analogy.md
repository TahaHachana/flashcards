## Subquery Temporary Table Analogy

How is a subquery similar to and different from a temporary table?

---

Similarities:
- Both create a temporary result set
- Both can be queried/joined like regular tables
- Both hold data in memory (typically)
- Both can have aliases/names

Differences:

Subquery:
- Statement scope: Exists only during query execution
- Automatically created and destroyed
- Cannot be referenced by other queries
- No explicit CREATE/DROP syntax
- Ideal for one-time, query-specific logic

Temporary table:
- Session scope: Exists until session ends or explicit DROP
- Explicitly created with CREATE TEMPORARY TABLE
- Can be referenced by multiple queries in session
- Can be indexed for performance
- Ideal for multi-step operations or complex workflows

Use subquery when: Single-query, one-time calculation
Use temp table when: Multi-query workflow, complex ETL, need indexes

