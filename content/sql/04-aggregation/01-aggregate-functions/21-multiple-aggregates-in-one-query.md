## Multiple Aggregates in One Query

Can you use multiple different aggregate functions in the same SELECT statement? What is the result grain?

---

Yes, you can use multiple aggregate functions in one SELECT statement. Example: SELECT COUNT(*), AVG(amount), MAX(amount), MIN(amount) FROM payment. All aggregates operate on the same group(s), so with implicit grouping you get one row with all the statistics, or with explicit grouping you get one row per group containing all aggregates for that group.

