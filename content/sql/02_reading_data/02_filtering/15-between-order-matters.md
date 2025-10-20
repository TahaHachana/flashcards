## BETWEEN Order Matters

Does the order of values matter in BETWEEN? What happens if you reverse them?

---

Order matters! Smaller value must come first.

Correct:
```sql
WHERE age BETWEEN 18 AND 65  -- 18 to 65
```

Wrong:
```sql
WHERE age BETWEEN 65 AND 18  -- No results!
```

Why wrong version fails:
It's interpreted as: `age >= 65 AND age <= 18`
No value can be both >= 65 and <= 18, so no rows match.

Rule: Always put the lower bound first, higher bound second.

```sql
-- Right:
WHERE price BETWEEN 10 AND 100

-- Wrong:
WHERE price BETWEEN 100 AND 10  -- Returns nothing
```

