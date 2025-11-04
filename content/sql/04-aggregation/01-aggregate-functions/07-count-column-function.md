## COUNT Column Function

What does COUNT(column) count, and how does it differ from COUNT(*)?

---

COUNT(column) counts only the rows where the specified column has a non-NULL value. Unlike COUNT(*) which counts all rows, COUNT(column) ignores any rows where that column is NULL. Example: if a customers table has 304 rows but only 268 have phone numbers, COUNT(*) returns 304 while COUNT(phone) returns 268.

