## Cannot Use Aliases in GROUP BY

Why can't you use column aliases in the GROUP BY clause? How do you work around this?

---

You can't use aliases because GROUP BY is processed before SELECT, so the aliases don't exist yet. Workaround: repeat the expression in GROUP BY. Example: SELECT YEAR(order_date) AS order_year, COUNT(*) FROM orders GROUP BY YEAR(order_date). You must write YEAR(order_date) twice - once in SELECT (creating the alias) and once in GROUP BY (doing the grouping).

