## Multiple References To Same CTE

How can a CTE be referenced multiple times, and why is this valuable?

---

A CTE can be referenced multiple times without repeating its definition.

Example - Self-join for month-over-month comparison:
WITH monthly_sales AS (
  SELECT month, SUM(amount) as total
  FROM sales
  GROUP BY month
)
SELECT 
  current.month,
  current.total,
  previous.total as prev_month,
  current.total - previous.total as growth
FROM monthly_sales current
LEFT JOIN monthly_sales previous ON previous.month = current.month - 1;

Why valuable:
- DRY principle: Don't Repeat Yourself
- Single definition means single point of maintenance
- If calculation changes, change it once
- Database may optimize by calculating CTE once and reusing results
- Clearer intent than duplicating subquery logic

Contrast with subqueries: Would need to repeat the entire aggregation logic twice.

