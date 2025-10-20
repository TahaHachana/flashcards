## How Text Sorts

How does text sort in ORDER BY? What affects the sort order?

---

Text sorts alphabetically:
- Ascending: A, Apple, B, Banana, C, Cherry
- Descending: Z, Zebra, Y, Yellow, X, Xylophone

Factors affecting sort:
1. Case handling (usually case-insensitive, but database-dependent)
2. Special characters (sort before/after letters, varies by database)
3. Collation settings (how characters are compared)

Examples:
```sql
-- Ascending:
ORDER BY last_name
-- Result: Anderson, Brown, Chen, Davis

-- Descending:
ORDER BY last_name DESC
-- Result: Davis, Chen, Brown, Anderson
```

Note: Exact behavior (especially for accents, case, special chars) depends on database collation settings.

