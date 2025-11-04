## Aggregate Independence Across Groups

How do aggregate functions operate across different groups created by GROUP BY?

---

Aggregate functions operate independently within each group - they don't interact across groups. Each group gets its own separate calculation as if it were the only data in the table. Example: GROUP BY customer_id with SUM(amount) calculates a separate sum for each customer's rows only, not a running total or anything involving other customers.

