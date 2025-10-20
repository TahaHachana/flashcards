## NULL In Comparisons

What happens when NULL is involved in comparisons? Why does this matter for filtering?

---

Any comparison with NULL results in NULL (not TRUE or FALSE):

```sql
NULL = 5      → NULL (not FALSE)
NULL <> 5     → NULL (not TRUE)
NULL > 5      → NULL
5 > NULL      → NULL
NULL = NULL   → NULL (even this!)
```

Impact on WHERE:
Only rows where condition is TRUE are included. NULL is treated as "not TRUE", so rows are excluded.

Example:
```sql
WHERE age > 30
```

Rows with:
- age = 35: TRUE → included
- age = 25: FALSE → excluded  
- age = NULL: NULL → excluded

This is why NULL values often disappear from filtered results.

