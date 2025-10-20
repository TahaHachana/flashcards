## Condition Evaluation Results

What three values can a condition evaluate to? Which rows are included in results?

---

Every condition evaluates to one of three values:

1. TRUE - Row passes this condition
2. FALSE - Row fails this condition  
3. NULL - Result is unknown (treated as "not TRUE")

Only rows where the overall WHERE condition is TRUE are included.

Example:
```sql
WHERE age >= 18 AND country = 'USA'
```

For each row:
- If age >= 18 is TRUE AND country = 'USA' is TRUE → Row included
- If either is FALSE → Row excluded
- If either is NULL → Row excluded (NULL is "not TRUE")

Key point: NULL is treated as FALSE for filtering purposes. Only TRUE rows make it through.

This is why rows with NULL values often disappear from filtered results.

