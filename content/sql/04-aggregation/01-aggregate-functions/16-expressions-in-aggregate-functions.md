## Expressions in Aggregate Functions

Can aggregate functions work on expressions, or only on simple columns? Give an example.

---

Aggregate functions can work on any expression that produces a value, not just simple columns. Example: MAX(return_date - rental_date) calculates the difference for each row, then finds the maximum of those calculated values. You can use arithmetic, functions, CASE statements, or any expression inside an aggregate function.

