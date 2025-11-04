## COUNT Star vs COUNT Column with NULLs

Given a table with 4 rows where one row has a NULL value in the 'val' column, what will COUNT(*) and COUNT(val) each return?

---

COUNT(*) will return 4 because it counts all rows regardless of NULL values. COUNT(val) will return 3 because it only counts rows where the val column has a non-NULL value. This difference is why COUNT(*) is the only aggregate function that "includes" NULLs - it's actually counting rows, not values.

