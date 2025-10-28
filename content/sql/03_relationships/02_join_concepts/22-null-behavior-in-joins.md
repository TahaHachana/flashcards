## NULL Behavior in JOINs

How do NULLs behave in JOIN conditions, and what's an important consideration when joining on nullable columns?

---

NULL never equals NULL in SQL comparison logic, so `NULL = NULL` evaluates to FALSE (or UNKNOWN). This means rows with NULL values in JOIN columns won't match each other, even if both sides have NULL. When joining on nullable foreign keys, rows with NULL foreign keys will appear in LEFT JOINs from the left table but won't match any right table rows.

