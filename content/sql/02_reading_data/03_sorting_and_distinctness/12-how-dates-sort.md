## How Dates Sort

How do dates sort in ORDER BY? Give examples.

---

Dates sort chronologically:
- Ascending: Oldest to newest (1990-01-01, 2000-01-01, 2024-01-01)
- Descending: Newest to oldest (2024-01-01, 2000-01-01, 1990-01-01)

Examples:
```sql
-- Oldest orders first:
ORDER BY order_date ASC
-- Result: 2020-01-15, 2021-03-20, 2024-10-01

-- Most recent orders first:
ORDER BY order_date DESC
-- Result: 2024-10-01, 2021-03-20, 2020-01-15
```

Common patterns:
```sql
-- Recent activity first:
ORDER BY updated_at DESC

-- Chronological history:
ORDER BY transaction_date ASC
```

Dates must be stored as DATE/DATETIME type for correct chronological sorting.

