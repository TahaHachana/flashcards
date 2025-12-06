## UNION ALL Operator Purpose

What does the UNION ALL operator do, and why is it generally preferred over UNION?

---

UNION ALL combines two result sets and keeps all rows, including duplicates.

Set theory representation:
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
A UNION ALL B: {1, 2, 3, 4, 3, 4, 5, 6}  -- All rows, duplicates included

Key characteristics:
- Keeps all rows, including duplicates
- No sorting or duplicate checking
- MUCH faster and more efficient than UNION
- Row count = sum of all input result sets

Performance advantage: Doesn't need to check for duplicates or sort, making it significantly faster for large result sets.

Why generally preferred:
- Default choice unless you specifically need deduplication
- More explicit about intent
- Better performance

Example:
SELECT first_name, last_name FROM customer  -- 599 rows
UNION ALL
SELECT first_name, last_name FROM actor;    -- 200 rows
-- Result: All 799 rows (599 + 200)

