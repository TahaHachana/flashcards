## Foreign Key Properties

What are the key properties of foreign keys? Can they be NULL? Can they repeat?

---

Foreign key properties:

1. References a primary key in another table
2. CAN be NULL (indicates no relationship, if allowed)
3. CAN repeat (many rows can point to same parent)
4. Must match a valid primary key value (or be NULL)

Example:
```
Orders:
order_id | customer_id (FK)
---------|------------------
101      | 1                ← Points to customer 1
102      | 1                ← Points to customer 1 (repeat OK!)
103      | 2                ← Points to customer 2
104      | NULL             ← No customer (if allowed)
```

Unlike primary keys, foreign keys are not unique.

