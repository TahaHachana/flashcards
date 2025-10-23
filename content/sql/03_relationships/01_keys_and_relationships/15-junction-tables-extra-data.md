## Junction Tables With Extra Data

Can junction tables have columns beyond just the foreign keys? Give an example.

---

Yes! Junction tables often store additional information about the relationship.

Example - E-commerce OrderItems:
```
Orders:
order_id (PK) | customer_id | order_date

Products:
product_id (PK) | name | price

OrderItems (junction + extra data):
item_id (PK) | order_id (FK) | product_id (FK) | quantity | price_at_purchase
```

Extra columns:
- quantity: How many of this product in this order
- price_at_purchase: Price when ordered (might differ from current price)

Other examples:
- Enrollments: grade, enrollment_date
- Assignments: assigned_date, due_date, status
- Likes: timestamp, reaction_type

Junction tables are full tables that can store any relevant data about the relationship.

