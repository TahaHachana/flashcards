## Scalar Subquery Definition

What is a scalar subquery, and where can it be used?

---

A scalar subquery returns exactly one row with one column - a single value.

Can be used anywhere a single value is expected:
- Either side of comparison operators (=, <>, <, >, <=, >=)
- In the SELECT clause to calculate values
- In the ORDER BY clause for sorting
- In the VALUES clause of INSERT statements

Example: (SELECT MAX(customer_id) FROM customer) returns a single value like 599.

