## Direction of Relationships

In a relationship diagram, which direction does the arrow point? What does it represent?

---

Arrow points FROM foreign key TO primary key.

Visual:
```
Customers         Orders
┌──────────┐      ┌──────────┐
│ id (PK)  │←────┤ id (PK)  │
│ name     │      │ cust_id  │ (FK)
└──────────┘      │ product  │
    ONE           └──────────┘
                      MANY
```

Arrow direction: Orders.customer_id → Customers.id

Reading the relationship:
- Arrow starts at foreign key (many side)
- Arrow points to primary key (one side)
- Shows: "Many orders point to one customer"

Remember: FK on MANY side, arrow points to ONE side.

