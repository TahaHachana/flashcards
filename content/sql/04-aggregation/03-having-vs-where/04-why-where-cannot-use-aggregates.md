## Why WHERE Cannot Use Aggregates

Why does this query fail: `SELECT customer_id, COUNT(*) FROM orders WHERE COUNT(*) > 10 GROUP BY customer_id;`?

---

It fails because WHERE is evaluated before GROUP BY, so aggregate values don't exist yet when WHERE runs. At the WHERE stage, SQL is still working with individual rows - groups haven't been created and COUNT() hasn't been calculated. You're trying to filter on information that doesn't exist yet. Use HAVING instead, which runs after aggregates are calculated.

