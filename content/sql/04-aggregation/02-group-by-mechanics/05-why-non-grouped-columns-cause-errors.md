## Why Non Grouped Columns Cause Errors

Why does this query fail: `SELECT customer_id, first_name, COUNT(*) FROM orders GROUP BY customer_id;`?

---

It fails because first_name is not in the GROUP BY clause and not aggregated. Each customer_id group might contain multiple orders, and SQL doesn't know which first_name value to display for the group. The fix is either: (1) add first_name to GROUP BY, or (2) aggregate it with something like MAX(first_name), though that's rarely what you actually want.

