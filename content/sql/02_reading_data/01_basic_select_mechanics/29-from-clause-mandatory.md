## FROM Clause Mandatory

Is the FROM clause always required in a SELECT statement? Are there any exceptions?

---

FROM is almost always required - you must tell the database where to get data.

Standard query:
```sql
SELECT name FROM customers;  -- FROM required
```

Exception (some databases):
Testing or calculating without a table:
```sql
-- PostgreSQL, Oracle require FROM:
SELECT 1 + 1 FROM dual;  -- dual is dummy table

-- MySQL, SQL Server allow:
SELECT 1 + 1;  -- No FROM needed
SELECT 'Hello', 42;
```

But for actual data retrieval, FROM is always required because the database needs to know: "from which table?"

Best practice: Always use FROM when retrieving actual data.

