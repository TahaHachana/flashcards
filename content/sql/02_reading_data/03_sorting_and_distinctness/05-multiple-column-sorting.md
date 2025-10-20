## Multiple Column Sorting

How does sorting by multiple columns work? What is the second column used for?

---

Multiple columns: first column sorts primarily, second breaks ties.

```sql
ORDER BY last_name, first_name
```

How it works:
1. Sort by last_name first
2. When last_name values are identical (tie), use first_name

Example result:
```
last_name  | first_name
-----------|------------
Anderson   | Alice
Anderson   | Bob        ← Same last name, sorted by first
Johnson    | Carol
Smith      | David
Smith      | Emma       ← Same last name, sorted by first
Smith      | Frank
```

The second column only matters when first column has duplicates.

Called a "tiebreaker" column.

