## WHERE Clause Purpose

What does the WHERE clause do? Describe its role in the query processing order.

---

WHERE filters rows based on conditions. It determines which rows are included in the result.

```sql
SELECT first_name, last_name
FROM customers
WHERE age >= 18;
```

Processing order:
1. FROM customers (start with table)
2. WHERE age >= 18 (filter rows - keeps only TRUE)
3. SELECT first_name, last_name (choose columns)

Mental model: WHERE is a filter that lets some rows through and blocks others, based on whether they meet your criteria.

Only rows where the condition evaluates to TRUE are included.

