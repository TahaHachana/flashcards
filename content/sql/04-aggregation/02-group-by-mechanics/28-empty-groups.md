## Empty Groups

If a value exists in your grouping column but has no matching rows after filtering with WHERE, will GROUP BY create an empty group for it?

---

No, GROUP BY only creates groups for values that actually exist in the filtered result set. If WHERE filters out all rows with a certain value, that value won't appear in the GROUP BY results. Example: if WHERE amount > 100 filters out all orders from customer 5, that customer won't appear in GROUP BY customer_id results, even though they exist in the customers table.

