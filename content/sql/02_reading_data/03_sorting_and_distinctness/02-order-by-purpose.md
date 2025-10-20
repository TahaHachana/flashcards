## ORDER BY Purpose

What does the ORDER BY clause do? When does it process in the query execution?

---

ORDER BY sorts your result set in a specified order.

Processing order:
```
1. FROM customers
2. WHERE age >= 18
3. SELECT first_name, last_name
4. ORDER BY last_name    ← Last step!
```

ORDER BY processes LAST, after all other clauses.

Example:
```sql
SELECT first_name, last_name
FROM customers
ORDER BY last_name;
```

What happens:
1. Retrieve data (FROM, WHERE, SELECT)
2. Sort the entire result by last_name
3. Return sorted results

ORDER BY is the only way to guarantee a specific order.

