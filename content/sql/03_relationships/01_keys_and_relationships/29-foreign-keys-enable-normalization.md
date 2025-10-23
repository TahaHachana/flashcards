## Foreign Keys Enable Normalization

How do foreign keys make normalization possible? What would happen without them?

---

Foreign keys are what make normalized databases work.

Without foreign keys:
- Must store all related data in one table
- Massive redundancy (repeat customer info in every order)
- Update anomalies (change email in 100 places)
- Can't separate concerns

With foreign keys:
- Can separate entities into logical tables
- Store each fact once
- Maintain relationships through IDs
- Update in one place

Example:
```
WITHOUT FKs (denormalized):
Orders: order_id | cust_name | cust_email | cust_phone | product
        Repeat customer info in every order!

WITH FKs (normalized):
Customers: customer_id | name | email | phone
Orders: order_id | customer_id (FK) | product
        Reference customer once!
```

Foreign keys are the glue that holds normalized databases together.

