## WHERE with GROUP BY Process

When you use WHERE with GROUP BY, what is the process that occurs?

---

Process: (1) FROM gets data, (2) WHERE filters rows (before grouping), (3) GROUP BY groups the filtered rows, (4) Aggregates are calculated on each group, (5) SELECT returns results. Example: WHERE state = 'CA' filters to California customers first, then GROUP BY customer_id groups only those California customers, reducing the data that needs grouping.

