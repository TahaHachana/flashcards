## COUNT Star Function

What does COUNT(*) count, and does it include rows with NULL values?

---

COUNT(*) counts the total number of rows in the group, including rows where all columns are NULL or some columns are NULL. It counts rows, not values. This is different from COUNT(column), which only counts non-NULL values in a specific column.

