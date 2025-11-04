## CASE Expression Grouping

Can you use a CASE expression in GROUP BY? Give an example of when this is useful.

---

Yes, you can group by CASE expressions to create custom categories. Example: GROUP BY CASE WHEN price < 10 THEN 'Budget' WHEN price < 50 THEN 'Standard' ELSE 'Premium' END. This creates three groups based on price ranges. You must repeat the entire CASE expression in both SELECT and GROUP BY since you can't use the alias.

