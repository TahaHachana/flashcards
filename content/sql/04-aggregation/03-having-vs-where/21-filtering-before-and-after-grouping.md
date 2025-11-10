## Filtering Before and After Grouping

Explain the concept of "filtering twice" when using both WHERE and HAVING.

---

WHERE filters the input data (before grouping) and HAVING filters the output groups (after aggregation). This is two separate filtering stages. Example: WHERE filters 10,000 orders to 1,000 California orders, then GROUP BY creates 50 customer groups, then HAVING filters to 10 high-spending groups. Each filter serves a different purpose at a different stage.

