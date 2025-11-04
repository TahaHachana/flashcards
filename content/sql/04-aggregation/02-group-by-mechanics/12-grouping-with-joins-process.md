## Grouping with JOINs Process

When you GROUP BY after a JOIN, what is the process that occurs?

---

Process: (1) JOIN creates a result set combining data from multiple tables, (2) GROUP BY separates this joined data into buckets based on grouping columns, (3) aggregate functions operate on each bucket, (4) result shows one row per group with aggregated statistics. Example: JOIN customers and orders, then GROUP BY customer_id to get order counts per customer.

