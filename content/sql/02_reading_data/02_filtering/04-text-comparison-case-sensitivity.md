## Text Comparison Case Sensitivity

Are text comparisons in WHERE clause case-sensitive? Give examples.

---

String values are ALWAYS case-sensitive in most databases:

```sql
WHERE country = 'USA'     -- Matches 'USA' only
WHERE country = 'usa'     -- Matches 'usa' only
WHERE country = 'Usa'     -- Matches 'Usa' only
```

'USA' ≠ 'usa' ≠ 'Usa'

To make case-insensitive:
```sql
-- Use UPPER or LOWER:
WHERE UPPER(country) = 'USA'  -- Matches 'usa', 'USA', 'Usa'

-- PostgreSQL: Use ILIKE instead of LIKE
WHERE country ILIKE 'usa'
```

Important: Case-sensitivity applies to values, not column names (those are usually case-insensitive).

