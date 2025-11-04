## The Fundamental SELECT Rule with GROUP BY

What is the fundamental rule about what you can SELECT when using GROUP BY?

---

You can only SELECT: (1) columns that appear in the GROUP BY clause, OR (2) aggregate functions. You cannot SELECT columns that don't appear in GROUP BY and aren't aggregated. This is because such columns can have multiple different values within a group, and SQL doesn't know which one to display.

