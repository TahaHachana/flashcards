## INNER JOIN Mental Model

Using the mental model of "only the overlap," what happens to customers with no orders and orders with no matching customer in an INNER JOIN between customers and orders tables?

---

Both are excluded from the results. Customers with no orders don't appear because there's no matching order row. Orders with no matching customer don't appear because there's no matching customer row. Only customers who have orders (the overlap) appear in the result set.

