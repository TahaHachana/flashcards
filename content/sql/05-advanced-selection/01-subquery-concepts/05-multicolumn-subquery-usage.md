## Multicolumn Subquery Usage

How do you use a multicolumn subquery, and what must match between the left side and the subquery?

---

A multicolumn subquery returns multiple columns and rows (table-like structure).

Usage pattern:
WHERE (col1, col2) IN (SELECT col_a, col_b FROM table)

Requirements:
- List columns in parentheses on the left side
- Columns must be in the same order as the subquery returns them
- The comparison checks if the combination exists in subquery results

Example: WHERE (actor_id, film_id) IN (SELECT actor_id, film_id FROM ...)

