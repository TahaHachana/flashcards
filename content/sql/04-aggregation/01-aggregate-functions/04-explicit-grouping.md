## Explicit Grouping

What is explicit grouping and how does it differ from implicit grouping?

---

Explicit grouping occurs when you use a GROUP BY clause to create named buckets of rows. Instead of one implicit group containing all rows, you get multiple explicit groups (one per unique value or combination of values). Each group gets its own aggregate calculation, resulting in one row per group. Example: GROUP BY customer_id creates one group per customer.

