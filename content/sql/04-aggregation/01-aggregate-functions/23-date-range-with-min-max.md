## Date Range with MIN and MAX

How can you use MIN() and MAX() with date columns to find the time span of your data?

---

Use MIN() to find the earliest date and MAX() to find the latest date, then subtract them for the span. Example: SELECT MIN(order_date) AS first_order, MAX(order_date) AS latest_order, MAX(order_date) - MIN(order_date) AS days_span FROM orders. This shows the date range covered by your dataset.

