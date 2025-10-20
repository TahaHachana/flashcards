## NOT Operator Logic

What does the NOT operator do? Give examples of its use.

---

NOT reverses a condition (TRUE becomes FALSE, FALSE becomes TRUE).

```sql
WHERE NOT country = 'USA'
-- Same as:
WHERE country <> 'USA'
```

Truth table:
```
NOT TRUE  = FALSE
NOT FALSE = TRUE
NOT NULL  = NULL
```

Examples:
```sql
-- Customers who are NOT under 18:
WHERE NOT (age < 18)
-- Same as: WHERE age >= 18

-- Products NOT discontinued:
WHERE NOT discontinued

-- Exclude specific countries:
WHERE NOT (country = 'USA' OR country = 'Canada')
-- Same as: WHERE country <> 'USA' AND country <> 'Canada'
```

Useful for negating complex conditions.

