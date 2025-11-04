## Cannot Mix Without GROUP BY

Why can't you include a non-aggregated column in a SELECT statement that uses aggregate functions without GROUP BY?

---

Without GROUP BY, there's one implicit group containing all rows. If you try to select a non-aggregated column like customer_id, SQL doesn't know which customer_id value to show since the group contains multiple different customers. You must either aggregate every column (COUNT, SUM, etc.) or use GROUP BY to separate the data into groups where each group has one value for that column.

