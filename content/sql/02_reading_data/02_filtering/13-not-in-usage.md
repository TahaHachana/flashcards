## NOT IN Usage

How does NOT IN work? What's the caveat about NULL values?

---

NOT IN excludes rows matching any value in the list.

```sql
WHERE country NOT IN ('USA', 'Canada')
```

Excludes USA and Canada, includes everything else.

Equivalent to:
```sql
WHERE country <> 'USA' AND country <> 'Canada'
```

WARNING about NULL:
If the list contains NULL, NOT IN can produce unexpected results:

```sql
WHERE id NOT IN (1, 2, NULL)
-- Might return no rows!
```

Why: `id <> NULL` is always NULL, and NULL in an AND chain makes everything NULL.

Best practice: Avoid NOT IN with lists that might contain NULL. Use NOT EXISTS or ensure no NULLs.

