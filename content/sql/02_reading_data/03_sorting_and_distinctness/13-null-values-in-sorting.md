## NULL Values In Sorting

Where do NULL values appear when you ORDER BY a column containing NULLs? How can you control this?

---

NULL placement varies by database:

Most common (MySQL, SQL Server, SQLite):
- NULLs appear first in both ASC and DESC

PostgreSQL, Oracle:
- ASC: NULLs last
- DESC: NULLs first

Controlling NULL position:

PostgreSQL/Oracle:
```sql
ORDER BY age NULLS LAST
ORDER BY age NULLS FIRST
```

SQL Server/MySQL (workaround):
```sql
-- Force NULLs last:
ORDER BY CASE WHEN age IS NULL THEN 1 ELSE 0 END, age

-- Force NULLs first:
ORDER BY CASE WHEN age IS NULL THEN 0 ELSE 1 END, age DESC
```

Best practice: Test your database's behavior or explicitly control NULL placement.

