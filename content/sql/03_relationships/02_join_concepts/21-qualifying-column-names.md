## Qualifying Column Names

What does it mean to "qualify" a column name, and when should you do it?

---

Qualifying a column means prefixing it with its table name or alias (e.g., `customers.customer_id` or `c.customer_id`). You MUST qualify column names when the same column name exists in multiple joined tables to avoid ambiguity errors. It's best practice to always qualify columns in JOINs for clarity, even when not strictly required.

