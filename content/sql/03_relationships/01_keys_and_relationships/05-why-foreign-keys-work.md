## Why Foreign Keys Work

Explain how foreign keys solve the normalization problem. Compare storing customer info in Orders vs using a foreign key.

---

Without foreign key (BAD):
```
Orders:
order_id | customer_name | customer_email    | product
101      | Alice Smith   | alice@example.com | Widget
102      | Alice Smith   | alice@example.com | Gadget
```
Problem: Alice's info repeated (redundancy, update anomalies)

With foreign key (GOOD):
```
Customers:
customer_id | name        | email
1           | Alice Smith | alice@example.com

Orders:
order_id | customer_id (FK) | product
101      | 1                | Widget
102      | 1                | Gadget
```

Benefits:
- Alice's info stored once
- Update in one place
- No redundancy
- Relationship maintained

