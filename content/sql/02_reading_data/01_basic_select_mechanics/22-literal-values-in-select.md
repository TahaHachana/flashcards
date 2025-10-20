## Literal Values in SELECT

What are literal values in SELECT? Give examples of when you'd use them.

---

Literal values are constants that appear directly in your query.

Examples:
```sql
SELECT 'Hello World';           -- String literal
SELECT 42;                      -- Number literal
SELECT 3.14;                    -- Decimal literal
SELECT 'Active' AS status, name FROM customers;  -- Combined
```

Use cases:
1. Testing queries
2. Adding fixed values to results
3. Creating labels or categories
4. Combining with actual data:
```sql
SELECT name, 'Customer' AS type FROM customers;
```

Result:
```
name    | type
--------|----------
Alice   | Customer
Bob     | Customer
```

Every row gets the same literal value.

