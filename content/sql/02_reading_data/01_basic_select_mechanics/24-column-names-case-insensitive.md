## Column Names Are Case Insensitive

Are column and table names case-sensitive in SQL? Are there exceptions?

---

Usually case-insensitive:
```sql
SELECT FirstName FROM Customers;
-- Same as:
SELECT firstname FROM customers;
```

Works in most databases (MySQL, SQL Server, SQLite).

Exception: PostgreSQL with quoted identifiers
```sql
-- These are DIFFERENT in PostgreSQL:
SELECT "FirstName" FROM "Customers";  -- Case-sensitive
SELECT FirstName FROM Customers;      -- Case-insensitive
```

String values ALWAYS case-sensitive:
```sql
WHERE name = 'John'  -- Matches 'John' only, not 'john'
```

Best practice: Be consistent with casing to avoid confusion, even though it usually doesn't matter.

