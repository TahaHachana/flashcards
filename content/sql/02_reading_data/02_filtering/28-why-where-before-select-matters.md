## Why WHERE Before SELECT Matters

Explain with an example why it matters that WHERE processes before SELECT.

---

WHERE sees original table columns, not SELECT calculations.

This works:
```sql
SELECT first_name, last_name, age * 12 AS age_in_months
FROM customers
WHERE age >= 18;
-- WHERE can see 'age' because it's in the table
```

This doesn't work:
```sql
SELECT first_name, last_name, age * 12 AS age_in_months
FROM customers
WHERE age_in_months >= 216;
-- ERROR! age_in_months doesn't exist yet
```

Fix: Repeat the calculation in WHERE:
```sql
SELECT first_name, last_name, age * 12 AS age_in_months
FROM customers
WHERE age * 12 >= 216;
-- Now it works
```

Processing order:
1. FROM - table available
2. WHERE - sees table columns, not aliases
3. SELECT - creates aliases

This is why WHERE can't use SELECT aliases.

