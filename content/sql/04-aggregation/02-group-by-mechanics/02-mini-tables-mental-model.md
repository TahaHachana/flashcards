## Mini Tables Mental Model

Describe the "mini-tables" mental model for understanding GROUP BY.

---

GROUP BY temporarily splits your table into separate mini-tables, one for each group. Each mini-table contains only the rows that belong to that group. Aggregate functions then run on each mini-table separately. Finally, SQL combines the results into one result set with one row per mini-table. Example: GROUP BY customer_id creates one mini-table per customer, each containing only that customer's rows.

