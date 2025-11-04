## When to Use COUNT DISTINCT

In a payment table with multiple payments per customer, what's the difference between COUNT(customer_id) and COUNT(DISTINCT customer_id), and when would you use each?

---

COUNT(customer_id) counts total payments (including multiple payments from the same customer), while COUNT(DISTINCT customer_id) counts unique customers. Use COUNT(customer_id) when you want to know "how many transactions," and COUNT(DISTINCT customer_id) when you want to know "how many different customers made purchases." The first might return 16,049, the second 599.

