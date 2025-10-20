## LIKE Pattern Examples

Give examples of LIKE patterns and explain what each matches.

---

```sql
-- Starts with 'A' (A, Apple, Arizona):
WHERE name LIKE 'A%'

-- Ends with 'son' (Johnson, Anderson):
WHERE name LIKE '%son'

-- Contains 'john' anywhere (John, Johnny, St. John):
WHERE name LIKE '%john%'

-- Exactly 3 characters (Tom, Sue, Bob):
WHERE code LIKE '___'

-- At least 5 characters starting with 'A':
WHERE name LIKE 'A____%'  -- A + 4 more chars minimum

-- Phone format (555) ####:
WHERE phone LIKE '(555) ____'

-- Email with at least 3 chars before @:
WHERE email LIKE '___%@%'
```

Combining wildcards gives powerful pattern matching!

