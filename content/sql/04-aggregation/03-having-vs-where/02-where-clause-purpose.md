## WHERE Clause Purpose

What does the WHERE clause do, and when in the query process does it operate?

---

WHERE filters individual rows before any grouping happens. It operates on raw data, deciding which rows to include in the result set or which rows to group. It's a pre-grouping filter that reduces the dataset before aggregation begins. WHERE is evaluated after FROM but before GROUP BY.

