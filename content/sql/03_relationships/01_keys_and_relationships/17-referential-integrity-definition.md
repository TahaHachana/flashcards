## Referential Integrity Definition

What is referential integrity? Why does it matter?

---

Referential integrity: The guarantee that foreign keys always point to valid primary keys.

Rules enforced:
1. Can't insert orphaned rows (FK must match existing PK)
2. Can't delete parents with children (by default)
3. Can't update PK if FKs reference it (by default)

Example violations:
```sql
-- This fails if customer 999 doesn't exist:
INSERT INTO orders (customer_id) VALUES (999);  -- ERROR!

-- This fails if customer 1 has orders:
DELETE FROM customers WHERE customer_id = 1;  -- ERROR!
```

Why it matters:
- Prevents orphaned data
- Maintains relationship validity
- Ensures data consistency

Mental model: Foreign keys are contracts that guarantee relationships stay valid.

