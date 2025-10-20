## DISTINCT Purpose

What does DISTINCT do? Give an example of the problem it solves.

---

DISTINCT removes duplicate rows from results.

Without DISTINCT:
```sql
SELECT country FROM customers;
```
Returns:
```
USA
Canada
USA
USA
Mexico
Canada
USA
```
Many duplicates!

With DISTINCT:
```sql
SELECT DISTINCT country FROM customers;
```
Returns:
```
USA
Canada
Mexico
```
One of each unique value.

Use cases:
- Getting unique values for dropdowns
- Finding all categories/types
- Counting unique values
- Removing duplicate results

