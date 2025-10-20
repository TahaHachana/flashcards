## Combining Multiple Filter Patterns

Create a WHERE clause that finds: active customers from CA, NY, or TX, who registered in 2024, and have either an email or phone on file.

---

```sql
WHERE status = 'Active'
  AND state IN ('CA', 'NY', 'TX')
  AND registration_date BETWEEN '2024-01-01' AND '2024-12-31'
  AND (email IS NOT NULL OR phone IS NOT NULL);
```

Breaking it down:
1. `status = 'Active'` - Active customers only
2. `AND state IN ('CA', 'NY', 'TX')` - Specific states
3. `AND registration_date BETWEEN '2024-01-01' AND '2024-12-31'` - 2024 registrations
4. `AND (email IS NOT NULL OR phone IS NOT NULL)` - Have at least one contact method

Key points:
- All conditions connected with AND (must satisfy all)
- Parentheses around OR make intent clear
- Combines multiple filtering patterns:
  - Equality (status)
  - IN list (states)
  - Date range (registration)
  - NULL checking with OR (contact info)

