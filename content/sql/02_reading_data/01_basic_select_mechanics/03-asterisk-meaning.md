## What Asterisk Means in SELECT

What does SELECT * mean? Why should you avoid it in production code?

---

SELECT * means "all columns" (not all rows). It's shorthand for every column in the table.

Why avoid in production:
1. If table structure changes (new column added), code might break
2. Retrieves unnecessary data, wasting resources
3. Makes code unclear (what columns are actually used?)
4. Performance: Usually don't need every column
5. Not explicit about requirements

Better: List specific columns you need.

