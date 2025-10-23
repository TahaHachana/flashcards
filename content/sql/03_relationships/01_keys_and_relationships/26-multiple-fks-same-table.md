## Multiple Foreign Keys Same Table

Can one table have multiple foreign keys? Give an example.

---

Yes! A table can have foreign keys to multiple different tables.

Example - Orders table:
```
Customers:
customer_id (PK) | name

Employees:
employee_id (PK) | name

ShippingAddresses:
address_id (PK) | street | city

Orders:
order_id (PK) | customer_id (FK) → Customers
              | employee_id (FK) → Employees  
              | ship_address_id (FK) → ShippingAddresses
              | order_date
```

Each order has:
- One customer (who placed it)
- One employee (who processed it)
- One shipping address

Multiple relationships from one table - perfectly normal and common!

