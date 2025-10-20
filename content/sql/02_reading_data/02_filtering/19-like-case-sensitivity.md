## LIKE Case Sensitivity

Is LIKE case-sensitive? How does this vary by database?

---

Case sensitivity varies by database:

Usually case-insensitive:
- MySQL / MariaDB
- SQL Server

Usually case-sensitive:
- PostgreSQL

Examples:
```sql
WHERE last_name LIKE 'smith'
```

MySQL/SQL Server: Matches 'Smith', 'SMITH', 'smith'
PostgreSQL: Matches only 'smith'

PostgreSQL solution - use ILIKE:
```sql
WHERE last_name ILIKE 'smith'  -- Case-insensitive
```

Or use UPPER/LOWER:
```sql
WHERE UPPER(last_name) LIKE 'SMITH'  -- Works everywhere
```

Best practice: Don't assume - test your database's behavior or use UPPER/LOWER for consistency.

