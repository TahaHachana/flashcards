## Set Operations Adding Identifying Columns Pattern

What is the pattern for adding identifying columns in set operations, and why is it useful?

---

Pattern: Add literal columns to track the source of data.

Example:
SELECT first_name, last_name, 'CUST' AS type
FROM customer
UNION ALL
SELECT first_name, last_name, 'ACTR' AS type
FROM actor;

The type column identifies where each row came from:
- 'CUST' = from customer table
- 'ACTR' = from actor table

Benefits:

1. Interpretation: Helps understand the source of each row in results

2. Filtering: Can filter combined results by source
   WHERE type = 'CUST'

3. Grouping: Can aggregate by source
   GROUP BY type

4. Reporting: Include source in reports
   "Show me counts by source type"

5. Debugging: Quickly see data distribution across sources

Common variations:
- 'Employee', 'Customer', 'Contractor' (descriptive names)
- 1, 2, 3 (numeric codes)
- 'US', 'EU', 'APAC' (regions)

Best practice: Use descriptive strings rather than codes for readability.

