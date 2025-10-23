## Cannot Insert Orphaned Rows

Why can't you insert a row with a foreign key that doesn't match any primary key? Give an example.

---

Referential integrity prevents orphaned rows (children without parents).

Example:
```sql
Customers:
customer_id | name
1           | Alice
2           | Bob

-- This fails:
INSERT INTO orders (order_id, customer_id, product)
VALUES (105, 999, 'Widget');
-- ERROR: customer_id 999 doesn't exist!
```

Why this matters:
- Order 105 would reference non-existent customer 999
- Creates "orphaned" row - order with no customer
- Breaks relationship integrity
- Makes data unreliable

Must insert valid customer_id (1 or 2), or NULL if allowed.

This is referential integrity protecting your data.

