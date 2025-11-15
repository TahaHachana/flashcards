## Correlated Subquery Performance

What are the performance characteristics and mitigation strategies for correlated subqueries?

---

Performance characteristics:
- Can be expensive: Execute once per outer row
- 599 outer rows = 599 subquery executions
- Execution time grows linearly with outer query size
- Often the bottleneck in slow queries

Mitigation strategies:

1. Add indexes on columns used in correlation
   - Index columns in WHERE clause of subquery

2. Use EXISTS instead of IN when checking existence
   - Can short-circuit after finding first match

3. Consider JOINs or window functions as alternatives
   - Especially for large datasets

4. Test with realistic data volumes
   - Performance issues may not appear with small test data

When correlated is still best: Checking existence, complex per-row calculations where logic is clearest as correlated subquery.

