## Cannot Delete Parents With Children

What happens (by default) if you try to delete a row that has foreign keys pointing to it?

---

Default behavior: DELETE RESTRICTED - cannot delete parent if children exist.

Example:
```sql
-- Customer 1 has orders:
Orders:
order_id | customer_id (FK)
101      | 1
102      | 1

-- This fails:
DELETE FROM customers WHERE customer_id = 1;
-- ERROR: Cannot delete because orders reference this customer
```

Why:
- Deleting customer 1 would orphan orders 101 and 102
- They would point to non-existent customer
- Violates referential integrity

Solutions:
1. Delete children first, then parent
2. Use ON DELETE CASCADE (deletes children automatically)
3. Use ON DELETE SET NULL (sets FK to NULL)

Default (RESTRICT) is safest - forces you to handle children explicitly.

