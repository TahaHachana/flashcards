## Why Aggregate Error in WHERE

What error message appears when you try to use an aggregate function in WHERE, and what does it mean?

---

Error: "Invalid use of group function" or "aggregate functions are not allowed in WHERE". Meaning: You're trying to use COUNT, SUM, AVG, etc. in the WHERE clause, but aggregates can't be calculated until after GROUP BY creates groups. WHERE runs before GROUP BY, so aggregates don't exist yet. Move the condition to HAVING instead.

