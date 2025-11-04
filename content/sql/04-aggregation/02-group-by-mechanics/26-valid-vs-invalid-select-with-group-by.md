## Valid vs Invalid SELECT with GROUP BY

Given `GROUP BY customer_id`, which of these SELECT clauses are valid: (a) customer_id, COUNT(*), (b) customer_id, order_id, COUNT(*), (c) customer_id, MAX(order_id), COUNT(*)?

---

Valid: (a) and (c). Invalid: (b). Explanation: (a) selects the grouped column and an aggregate - valid. (c) selects the grouped column and aggregated values - valid because MAX(order_id) collapses multiple order_ids to one value. (b) is invalid because order_id isn't in GROUP BY and isn't aggregated - each customer has multiple orders and SQL doesn't know which to show.

