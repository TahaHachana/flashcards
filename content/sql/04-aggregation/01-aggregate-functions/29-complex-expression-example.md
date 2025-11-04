## Complex Expression Example

Can you calculate a discount percentage and then aggregate it? Write an example query that finds the average discount percentage.

---

Yes, you can calculate expressions and then aggregate them. Example: SELECT AVG((list_price - sale_price) / list_price * 100) AS avg_discount_pct FROM products. This calculates the discount percentage for each product row, then AVG() finds the average across all those calculated percentages. The expression is evaluated first, then aggregated.

