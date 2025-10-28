## LEFT JOIN Mental Model

In a LEFT JOIN between customers (left) and orders (right), what appears in the result set for a customer who has never placed an order?

---

The customer's information appears with all their column values intact, but all columns from the orders table will be NULL for that row. This preserves the customer record while indicating there are no associated orders.

