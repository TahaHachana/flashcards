## OR Operator Logic

How does the OR operator work? When is a row included?

---

OR requires AT LEAST ONE condition to be TRUE.

```sql
WHERE country = 'USA' OR country = 'Canada'
```

If either condition is TRUE, row is included.

Truth table:
```
TRUE  OR TRUE  = TRUE  → Row included
TRUE  OR FALSE = TRUE  → Row included
FALSE OR TRUE  = TRUE  → Row included
FALSE OR FALSE = FALSE → Row excluded
TRUE  OR NULL  = TRUE  → Row included
FALSE OR NULL  = NULL  → Row excluded
```

Example:
```sql
WHERE category = 'Electronics' OR category = 'Computers'
```

Returns products that are:
- Electronics OR
- Computers OR
- Both (if that were possible)

Only excluded if BOTH conditions are FALSE.

