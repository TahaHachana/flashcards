## Finding Unmatched Rows with LEFT JOIN

How can you use a LEFT JOIN to find rows in the left table that have NO matching rows in the right table?

---

Perform a LEFT JOIN and then add a WHERE clause that checks for NULL in the right table's primary key (or any NOT NULL column). For example: `WHERE orders.order_id IS NULL` would find all customers with no orders.

