## Single Column Grouping Result Count

If a column has 50 unique values, how many rows will GROUP BY that column produce?

---

It will produce 50 rows - one row per unique value in the grouping column. Each row represents one group and contains the group's value plus any aggregate calculations for that group. For example, if actor_id has 200 unique values, GROUP BY actor_id produces 200 rows showing statistics for each actor.

