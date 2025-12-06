## Set Operations Use Case Comparing Query Results

How can set operations be used to verify that two different queries produce identical results?

---

Use case: Verify that two different queries (e.g., optimized version vs original) produce the same results.

Using UNION (removes duplicates):
SELECT customer_id, total FROM query_version_1
UNION
SELECT customer_id, total FROM query_version_2;

Verification logic:
- If queries return identical data, UNION removes "duplicates" (second query's rows)
- Result row count = row count of first query
- If row counts differ, queries don't produce identical results

Using EXCEPT (shows differences):
-- Rows in query 1 but not in query 2
SELECT customer_id, total FROM query_version_1
EXCEPT
SELECT customer_id, total FROM query_version_2;
-- Should be empty if identical

-- Rows in query 2 but not in query 1
SELECT customer_id, total FROM query_version_2
EXCEPT
SELECT customer_id, total FROM query_version_1;
-- Should also be empty if identical

Using INTERSECT (shows overlap):
SELECT customer_id, total FROM query_version_1
INTERSECT
SELECT customer_id, total FROM query_version_2;
-- Row count should equal both individual queries if identical

Best practice: Use both directions of EXCEPT to catch all differences.

