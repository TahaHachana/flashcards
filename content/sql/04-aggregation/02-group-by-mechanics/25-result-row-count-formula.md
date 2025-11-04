## Result Row Count Formula

How do you determine how many rows a GROUP BY query will return?

---

The number of result rows equals the number of unique combinations of values in the GROUP BY columns. For single-column grouping, it's the number of distinct values in that column. For multi-column grouping, it's the number of distinct combinations. Example: GROUP BY state, city returns one row per unique (state, city) pair that exists in the data.

