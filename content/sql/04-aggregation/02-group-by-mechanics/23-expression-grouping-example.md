## Expression Grouping Example

Write a query pattern that groups sales by year and shows the total for each year.

---

SELECT YEAR(order_date) AS order_year, SUM(amount) AS total_sales FROM orders GROUP BY YEAR(order_date) ORDER BY order_year. This extracts the year from each order date, groups rows by that year value, sums amounts within each year, and returns one row per year showing the year and its total.

