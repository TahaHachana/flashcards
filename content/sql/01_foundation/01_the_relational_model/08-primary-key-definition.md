## Primary Key Definition

What is a primary key and what are its essential properties?

---

A primary key uniquely identifies each row in a table.

Properties:
- Must be unique (no two rows can have the same value)
- Cannot be NULL (every row must have a value)
- Should be unchanging (typically doesn't change once assigned)
- Should be meaningless (best practice: arbitrary ID rather than meaningful data)

Example: customer_id, order_id

