## One-to-Many JOIN Multiplication

What happens to row counts when you JOIN a customer table (one side) with an orders table (many side)?

---

Row multiplication occurs on the "one" side. Each customer row appears multiple times in the result - once for each of their orders. A customer with 5 orders appears in 5 rows. A customer with 0 orders doesn't appear at all (in INNER JOIN) or appears once with NULL order columns (in LEFT JOIN). This is normal behavior for one-to-many relationships.

