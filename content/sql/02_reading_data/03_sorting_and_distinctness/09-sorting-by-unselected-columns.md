## Sorting By Unselected Columns

Can you sort by columns that aren't in your SELECT clause? Give an example.

---

Yes! In most databases, you can sort by columns you didn't select.

```sql
SELECT first_name, last_name
FROM customers
ORDER BY registration_date DESC;
```

Returns names, but sorted by registration_date (even though it's not shown).

Use case: "Show me customer names, newest registrations first"

Why it works:
ORDER BY processes after SELECT but can still see original table columns in most databases.

Caveat: Doesn't work reliably with DISTINCT or GROUP BY - only sort by selected columns in those cases.

