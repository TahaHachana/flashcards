## Understanding Query Execution

Walk through the logical execution of this query:
```sql
SELECT name, age
FROM customers  
WHERE age >= 18
ORDER BY name;
```

---

Logical execution order:

1. FROM customers
   - Database starts with the customers table
   - All columns available

2. WHERE age >= 18
   - Filter to only rows where age is 18 or more
   - Still have all columns, fewer rows

3. SELECT name, age
   - From filtered rows, choose only name and age columns
   - Now have 2 columns (name, age)

4. ORDER BY name
   - Sort the results alphabetically by name

Result: Names and ages of adult customers, sorted alphabetically.

Understanding this order explains why WHERE can't see SELECT aliases and why ORDER BY can see them.

