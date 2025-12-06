## Set Operations Use Case Combining Aggregates

How can set operations be used to combine detail rows with summary rows in a single result set?

---

Use case: Combine detail aggregates with grand totals in one result set.

Example - Monthly sales plus grand total:
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(amount) AS total
FROM orders
GROUP BY DATE_TRUNC('month', order_date)

UNION ALL

SELECT NULL AS month,  -- NULL represents "all months"
       SUM(amount) AS total
FROM orders;

Result:
 month    | total
----------+--------
2024-01   | 15000
2024-02   | 17500
2024-03   | 16200
NULL      | 48700  ← Grand total

Pattern: Detail rows UNION ALL summary row(s)

Why this works:
- Detail query groups by time period
- Summary query doesn't group (gives grand total)
- NULL in month column indicates "all periods"
- UNION ALL combines them

Use cases:
- Reports with subtotals and grand totals
- Combining different aggregation levels
- Dashboard summaries with detail breakdowns

Alternative: Window functions with ROLLUP (database-dependent).

