## LIKE Operator Wildcards

What are the two wildcards used with LIKE? What does each match?

---

Two wildcards for pattern matching:

1. % (percent) - Matches any sequence of characters (including zero)
2. _ (underscore) - Matches exactly one character

Examples with %:
```sql
-- Names starting with 'A':
WHERE name LIKE 'A%'

-- Names ending with 'son':
WHERE name LIKE '%son'

-- Names containing 'john' anywhere:
WHERE name LIKE '%john%'

-- Emails from example.com:
WHERE email LIKE '%@example.com'
```

Examples with _:
```sql
-- Exactly 3 characters:
WHERE code LIKE '___'

-- Format A + any 2 chars + B:
WHERE pattern LIKE 'A__B'
```

% = any amount, _ = exactly one

