## Finding Recent Records Pattern

Give examples of common patterns for finding recent records using WHERE.

---

Recent records patterns:

1. Orders from 2024 onward:
```sql
WHERE order_date >= '2024-01-01'
```

2. Last 7 days:
```sql
WHERE created_at >= CURRENT_DATE - 7
```

3. This year:
```sql
WHERE YEAR(order_date) = 2024
-- Or better:
WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'
```

4. Last 30 days:
```sql
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAY
```

5. After specific timestamp:
```sql
WHERE updated_at > '2024-10-01 00:00:00'
```

These patterns are very common in reports and dashboards.

