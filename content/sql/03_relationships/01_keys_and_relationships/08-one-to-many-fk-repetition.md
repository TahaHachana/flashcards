## One-to-Many Foreign Key Repetition

In a one-to-many relationship, why can the foreign key value repeat in the "many" table? Is this data redundancy?

---

Foreign keys CAN and SHOULD repeat in the many table.

Example:
```
Orders:
order_id | customer_id (FK)
---------|------------------
101      | 1                ← Customer 1
102      | 1                ← Customer 1 (repeats!)
103      | 1                ← Customer 1 (repeats!)
104      | 2                ← Customer 2
```

Customer 1 has 3 orders, so customer_id = 1 appears 3 times.

Is this redundancy? NO!
- It's controlled redundancy (foreign keys)
- Necessary to maintain the relationship
- Only the ID repeats, not all customer data
- This is the whole point of foreign keys

Without repetition, you couldn't have one customer with multiple orders.

