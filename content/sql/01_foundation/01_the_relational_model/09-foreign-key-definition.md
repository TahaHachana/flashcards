## Foreign Key Definition

What is a foreign key and what is its purpose?

---

A foreign key is a column that references the primary key of another table.

Purpose: Creates relationships between tables

Properties:
- References a specific row in another table
- Can be NULL (indicating no relationship)
- Can repeat (many rows can reference the same parent)
- Must match a valid primary key (referential integrity)

Example: customer_id in Orders table pointing to customer_id in Customers table

