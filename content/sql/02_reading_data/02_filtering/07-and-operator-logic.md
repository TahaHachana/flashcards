## AND Operator Logic

How does the AND operator work? What must be true for a row to be included?

---

AND requires ALL conditions to be TRUE.

```sql
WHERE age >= 18 AND country = 'USA'
```

Both must be TRUE for row to be included.

Truth table:
```
TRUE  AND TRUE  = TRUE  → Row included
TRUE  AND FALSE = FALSE → Row excluded
FALSE AND TRUE  = FALSE → Row excluded
FALSE AND FALSE = FALSE → Row excluded
TRUE  AND NULL  = NULL  → Row excluded
FALSE AND NULL  = FALSE → Row excluded
```

Example:
```sql
WHERE age >= 21 AND state = 'CA'
```

Returns only customers who are:
- 21 or older AND
- In California

If either condition is FALSE, row is excluded.

