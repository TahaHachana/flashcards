## Combining ORDER BY And DISTINCT

Can you use ORDER BY and DISTINCT together? What's the processing order?

---

Yes! You can use both together.

```sql
SELECT DISTINCT country
FROM customers
ORDER BY country;
```

Returns unique countries in alphabetical order.

Processing order:
1. FROM customers
2. SELECT DISTINCT country (get unique countries)
3. ORDER BY country (sort them)

Example result:
```
country
-------
Canada
Mexico
USA
```

Important restriction:
ORDER BY columns should be in your SELECT when using DISTINCT:

```sql
-- This might fail:
SELECT DISTINCT country
FROM customers
ORDER BY registration_date;
```

Problem: Getting distinct countries, but sorting by registration_date. Which registration_date for each country?

Safe: Only sort by selected columns when using DISTINCT.

