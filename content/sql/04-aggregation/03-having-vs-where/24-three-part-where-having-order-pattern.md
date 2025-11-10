## Three Part WHERE HAVING ORDER Pattern

What's the pattern for: (1) filtering input rows, (2) grouping, (3) filtering groups, (4) sorting results?

---

WHERE <row conditions> GROUP BY <columns> HAVING <aggregate conditions> ORDER BY <sort criteria>. Example: WHERE status = 'active' GROUP BY customer_id HAVING COUNT(*) > 5 ORDER BY COUNT(*) DESC. Filters to active rows, groups by customer, keeps groups with 5+ rows, sorts by count descending.

