## Using CASE with COUNT

How can you use a CASE expression with COUNT() to conditionally count rows?

---

You can use CASE inside COUNT to count only rows meeting certain conditions. Example: COUNT(CASE WHEN amount > 5 THEN 1 END) counts only payments over 5. The CASE returns 1 for matching rows and NULL otherwise, and COUNT ignores the NULLs. This allows multiple conditional counts in one query without needing multiple WHERE clauses.

