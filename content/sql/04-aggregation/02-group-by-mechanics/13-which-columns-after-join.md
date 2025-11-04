## Which Columns After JOIN

After joining multiple tables, which columns can you use in GROUP BY?

---

You can group by columns from any table in the JOIN. Example: After joining customers and orders, you can GROUP BY customer_id (from customers), order_date (from orders), or both. You're not limited to just the joined table's columns - any column in any joined table is available for grouping.

