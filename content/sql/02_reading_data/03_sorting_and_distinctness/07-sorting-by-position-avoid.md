## Sorting By Position Avoid

Can you sort by column position? Why should you avoid it?

---

You CAN sort by position, but shouldn't:

```sql
SELECT last_name, first_name, age
FROM customers
ORDER BY 1, 2;  -- Sort by column 1 (last_name), then 2 (first_name)
```

Why avoid:
1. Not clear what you're sorting by
2. Breaks if you add/remove/reorder SELECT columns
3. Makes code harder to maintain
4. Obscures intent

Better:
```sql
ORDER BY last_name, first_name  -- Clear and maintainable
```

Use column names, not positions.

Exception: Acceptable in quick ad-hoc queries for exploration.

