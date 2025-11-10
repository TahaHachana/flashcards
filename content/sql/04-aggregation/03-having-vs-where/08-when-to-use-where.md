## When to Use WHERE

When should you use WHERE for filtering?

---

Use WHERE when filtering based on: (1) Column values in individual rows, (2) Conditions on raw data, (3) Data that exists before any aggregation. Examples: WHERE state = 'CA', WHERE order_date > '2024-01-01', WHERE status = 'active'. Use WHERE for row-level filters that should happen before grouping.

