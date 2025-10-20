## DISTINCT vs GROUP BY Preview

What's the difference between DISTINCT and GROUP BY? When do you use each?

---

They can produce the same result:

```sql
-- Using DISTINCT:
SELECT DISTINCT country FROM customers;

-- Using GROUP BY:
SELECT country FROM customers GROUP BY country;
```

Both return unique countries.

When to use which:

Use DISTINCT when:
- You just want unique values
- Simple uniqueness requirement
- No aggregation needed

Use GROUP BY when:
- You need aggregation (COUNT, SUM, AVG, etc.)
- Want to calculate values per group
- More complex grouping logic

Example needing GROUP BY:
```sql
-- Count customers per country (can't use DISTINCT):
SELECT country, COUNT(*) 
FROM customers 
GROUP BY country;
```

DISTINCT is simpler; GROUP BY is more powerful (covered in Phase 4).

