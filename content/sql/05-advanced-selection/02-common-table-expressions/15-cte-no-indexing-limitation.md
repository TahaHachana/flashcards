## CTE No Indexing Limitation

Why is the inability to index CTEs a limitation, and what's the solution?

---

Limitation: CTEs cannot have indexes, which can impact performance on large datasets.

Problem:
WITH large_cte AS (
  SELECT * FROM million_row_table WHERE condition1
)
SELECT * FROM large_cte WHERE condition2;  -- May be slow without index

Why it matters:
- Database must scan all CTE results for condition2
- Cannot use index to quickly find matching rows
- Performance degrades with large result sets

Solution: Use temporary table when indexing is needed:
CREATE TEMPORARY TABLE large_temp AS
SELECT * FROM million_row_table WHERE condition1;

CREATE INDEX idx_temp ON large_temp(column_for_condition2);

SELECT * FROM large_temp WHERE condition2;  -- Much faster with index

When to use temporary tables:
- Large intermediate result sets
- Multiple queries against same data
- Need to filter/join on specific columns efficiently

When CTEs are still fine:
- Small to medium result sets
- Single query usage
- Readability is priority over maximum performance

