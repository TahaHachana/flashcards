## Filtering on Unselected Columns

Can you filter (WHERE) on columns that aren't in your SELECT clause? Why or why not?

---

Yes! You can filter on columns you don't select.

Example:
```sql
SELECT first_name, last_name
FROM customers
WHERE registration_date >= '2024-01-01';
```

This returns only names, but filters by registration_date (which isn't shown).

Why this works:
Processing order:
1. FROM customers (all columns available)
2. WHERE registration_date >= '2024-01-01' (can see all columns)
3. SELECT first_name, last_name (narrows to these columns)

Use case: "Show me customer names for people who registered this year"

