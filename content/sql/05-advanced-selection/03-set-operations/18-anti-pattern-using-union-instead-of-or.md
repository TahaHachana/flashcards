## Anti Pattern Using UNION Instead Of OR

Why is using UNION on the same table with different filters an anti-pattern, and what's the better approach?

---

Anti-pattern - Using UNION for filtering same table:
SELECT first_name, last_name FROM customer
WHERE state = 'VIC'
UNION ALL
SELECT first_name, last_name FROM customer
WHERE dob < '1980-01-01';

Problems:
- Two separate table scans (inefficient)
- More complex execution plan
- Unnecessary duplicate work

Better approach - Use OR operator:
SELECT first_name, last_name FROM customer
WHERE state = 'VIC' OR dob < '1980-01-01';

Why better:
- Single table scan instead of two
- Simpler query execution plan
- Database can use indexes more effectively
- Clearer intent

When UNION is appropriate:
- Combining fundamentally different tables (not just different filters on the same table)
- Each query has complex JOINs to different tables
- Combining data from multiple sources (regional databases, current + archived)

Rule of thumb: If you're applying set operations to the same table with only filter differences, use OR/IN instead.

