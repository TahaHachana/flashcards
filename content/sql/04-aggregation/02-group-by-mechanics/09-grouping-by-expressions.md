## Grouping by Expressions

Can you GROUP BY calculated values instead of just columns? Give an example.

---

Yes, you can group by any expression that produces a value. Example: GROUP BY YEAR(order_date) calculates the year for each row, then creates one group per year value. Other examples: GROUP BY UPPER(state) for case-insensitive grouping, GROUP BY LEFT(last_name, 1) to group by first letter, or GROUP BY complex CASE expressions to create custom categories.

