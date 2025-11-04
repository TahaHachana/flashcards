## Grouping After Multiple JOINs

When you GROUP BY after joining three tables (customers, orders, products), what conceptually happens to the data?

---

The three tables are first joined into one large result set containing combined data from all three. Then GROUP BY separates this joined result into buckets based on the grouping columns (which can come from any of the three tables). Aggregates then calculate within each bucket. Example: after joining all three, GROUP BY customer_id creates one bucket per customer containing all their orders and associated product information.

