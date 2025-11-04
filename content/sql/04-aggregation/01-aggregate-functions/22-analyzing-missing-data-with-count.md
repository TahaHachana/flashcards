## Analyzing Missing Data with COUNT

How can you use COUNT to identify missing data in a table?

---

Compare COUNT(*) with COUNT(column) to find missing values. Example: SELECT COUNT(*) AS total, COUNT(phone) AS with_phone, COUNT(*) - COUNT(phone) AS without_phone FROM customers. The difference between COUNT(*) and COUNT(column) reveals how many rows have NULL in that column, helping identify data quality issues.

