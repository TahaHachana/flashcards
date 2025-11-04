## Implicit Grouping

What is implicit grouping and when does it occur?

---

Implicit grouping occurs when you use aggregate functions without a GROUP BY clause. SQL treats all rows as belonging to a single, invisible group. The aggregate functions calculate across all rows, and the result is one row containing grand totals. Example: SELECT COUNT(*) FROM payment returns one row summarizing all payments.

