## Foreign Key Definition

What is a foreign key? How does it differ from a primary key?

---

Foreign key: A column that references the primary key of another table.

Differences:
- Primary key: Uniquely identifies rows in THIS table
- Foreign key: Points to rows in ANOTHER table

Example:
```
Customers:
customer_id (PK) - identifies customers

Orders:
order_id (PK) - identifies orders
customer_id (FK) - points to Customers table
```

Foreign keys create relationships between tables.

Mental model: Foreign keys are "pointers" from one table to another.

