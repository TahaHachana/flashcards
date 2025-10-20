## Active Status Pattern

Give examples of common patterns for filtering by active/inactive status.

---

Active/inactive patterns:

1. Boolean flag:
```sql
WHERE is_active = TRUE
WHERE is_active = 1
WHERE is_deleted = 0
```

2. Status column:
```sql
WHERE status = 'Active'
WHERE status IN ('Active', 'Pending')
WHERE status <> 'Cancelled'
```

3. Date-based (no end date = still active):
```sql
WHERE end_date IS NULL
WHERE termination_date IS NULL
```

4. Date range (currently active):
```sql
WHERE start_date <= CURRENT_DATE 
  AND (end_date IS NULL OR end_date >= CURRENT_DATE)
```

5. Compound status:
```sql
WHERE is_active = TRUE
  AND status = 'Approved'
  AND deleted_at IS NULL
```

Choose pattern based on your data model.

