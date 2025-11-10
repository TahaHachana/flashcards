## Multiple Aggregate Conditions in HAVING

Can you use multiple aggregate conditions in HAVING? Give an example.

---

Yes, you can use multiple aggregate conditions with AND/OR. Example: HAVING COUNT(*) > 100 AND AVG(price) > 50 AND SUM(quantity) > 1000. This filters groups to only those meeting all three criteria: ordered frequently, high average price, and large total quantity. Each condition is evaluated independently on the group's aggregate values.

