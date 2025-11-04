## Implicit Grouping Result

How many rows does a query with implicit grouping return, and what does that row represent?

---

A query with implicit grouping (aggregates without GROUP BY) returns exactly one row, which represents the grand total or overall summary across all rows in the table. Example: SELECT COUNT(*), SUM(amount) FROM payment returns one row showing the total number of payments and total revenue across all customers.

