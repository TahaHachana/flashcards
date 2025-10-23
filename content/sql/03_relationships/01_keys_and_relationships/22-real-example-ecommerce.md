## Real Example E-commerce

Design an e-commerce system with Customers, Orders, and Products. Why do you need OrderItems as a junction table?

---

Structure:
```
Customers:
customer_id (PK) | name | email

Orders:
order_id (PK) | customer_id (FK) | order_date

Products:
product_id (PK) | name | price

OrderItems (junction):
item_id (PK) | order_id (FK) | product_id (FK) | quantity
```

Why OrderItems needed:
- One order contains many products → many-to-many
- One product appears in many orders → many-to-many
- Can't store multiple product_ids in Orders table
- OrderItems also stores quantity for each product in each order

Relationships:
- Customers → Orders: one-to-many (FK in Orders)
- Orders ↔ Products: many-to-many (via OrderItems)

Extra data in junction: quantity (how many of this product in this order)

