## DISTINCT On Entire Row

Does DISTINCT operate on individual columns or entire rows? Explain with an example.

---

DISTINCT operates on entire rows (all selected columns together).

```sql
SELECT DISTINCT last_name, first_name
FROM customers;
```

Returns unique combinations of (last_name, first_name).

Example:
```
last_name | first_name
----------|------------
Smith     | John       ← Unique combination
Smith     | Jane       ← Different first_name, included
Smith     | John       ← Duplicate combination, excluded
Jones     | John       ← Different last_name, included
```

Result: 3 rows (the duplicate Smith+John is removed)

Key point: It's not "distinct last names" or "distinct first names" - it's distinct COMBINATIONS of both.

DISTINCT evaluates the entire SELECT list as one unit.

