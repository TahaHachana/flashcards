## COUNT DISTINCT Function

What does COUNT(DISTINCT column) do and when would you use it?

---

COUNT(DISTINCT column) counts only the unique non-NULL values in a column, removing duplicates before counting. Use it when you want to know how many different values exist. Example: in a payment table, COUNT(customer_id) returns 16,049 (total payments) while COUNT(DISTINCT customer_id) returns 599 (unique customers).

