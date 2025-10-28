## JOIN Condition vs WHERE Filter

What is the difference between the JOIN condition (ON clause) and WHERE clause filters?

---

The ON clause determines HOW tables are matched together - it defines which rows from the tables should be combined. The WHERE clause filters the RESULT after the JOIN is complete. For INNER JOINs, the distinction matters less, but for OUTER JOINs it's critical: WHERE filters can remove the "preserved" rows that OUTER JOINs are designed to keep.

