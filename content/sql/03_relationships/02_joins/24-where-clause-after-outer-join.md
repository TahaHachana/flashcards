## WHERE Clause After OUTER JOIN

What happens when you apply a WHERE clause filter to the right table after a LEFT JOIN?

---

Filtering the right table in WHERE can eliminate the unmatched rows that LEFT JOIN was meant to preserve. If you filter `WHERE right_table.column = value`, rows where right_table columns are NULL (the unmatched rows) will be excluded. To avoid this, include `OR right_table.column IS NULL` in the WHERE condition, or move the filter into the ON clause if you want to filter BEFORE joining.

