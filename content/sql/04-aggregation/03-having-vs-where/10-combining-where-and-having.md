## Combining WHERE and HAVING

Can you use both WHERE and HAVING in the same query? What's the pattern?

---

Yes, you can and often should use both. Pattern: WHERE filters rows before grouping (reduces input data), then HAVING filters groups after aggregation (reduces output groups). This is like having two separate filters at different stages. Example: WHERE state = 'CA' (row filter) ... GROUP BY customer_id ... HAVING SUM(amount) > 1000 (group filter).

