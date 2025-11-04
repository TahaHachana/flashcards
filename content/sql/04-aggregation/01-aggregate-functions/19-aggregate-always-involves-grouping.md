## Aggregate Always Involves Grouping

True or False: Every aggregate query involves grouping, even if there's no GROUP BY clause. Explain.

---

True. Every aggregate query involves grouping. When there's no GROUP BY clause, there's implicit grouping - all rows are treated as one single group, and aggregates calculate across all rows (grand totals). When there is a GROUP BY clause, there's explicit grouping - rows are separated into multiple groups, and aggregates calculate separately for each group (subtotals).

