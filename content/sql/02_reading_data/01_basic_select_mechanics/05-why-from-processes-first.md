## Why FROM Processes First

Why does the FROM clause process before SELECT? What does this enable?

---

FROM processes first because the database needs to know which table to work with before it can do anything else.

Logical order:
1. FROM - Identify the table
2. WHERE - Filter rows from that table
3. SELECT - Choose columns from filtered rows
4. ORDER BY - Sort the results

This enables:
- Filtering on columns you don't select
- WHERE seeing all table columns
- Calculations and transformations in SELECT
- ORDER BY seeing both table columns and SELECT aliases

