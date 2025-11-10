## HAVING with Subquery

Can you use a subquery in HAVING? Give an example.

---

Yes. Example: HAVING AVG(amount) > (SELECT AVG(amount) FROM orders). This compares each group's average to the global average, filtering to groups above average. The subquery calculates the overall average, then HAVING uses it to filter groups. Useful for outlier detection or comparing groups to population statistics.

