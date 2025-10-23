## One-to-Many Foreign Key Placement

In a one-to-many relationship, which table holds the foreign key? Why?

---

The foreign key goes on the MANY side.

Example: Customers and Orders (one customer, many orders)
```
Customers (ONE):
customer_id (PK) | name

Orders (MANY):
order_id (PK) | customer_id (FK) | product
```

Why:
- Can't store multiple order IDs in one customer row (violates atomicity)
- Instead, each order stores which customer it belongs to
- Foreign key can repeat (customer_id appears multiple times in Orders)

Rule: Many points to One
Direction: FK on MANY side → PK on ONE side

