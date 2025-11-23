## CTE Materialization Versus Inlining

What is the difference between CTE materialization and inlining, and how does it affect performance?

---

Different databases handle CTE optimization differently:

Inline expansion (common):
- Database treats CTE like a macro
- CTE definition substituted into main query
- Optimized as one large query
- CTE code may execute multiple times if referenced multiple times

Materialization (sometimes):
- Database executes CTE once, stores results in memory
- Main query uses stored results
- CTE executes only once even if referenced multiple times

Example impact:
WITH expensive_cte AS (
  SELECT * FROM large_table WHERE complex_condition
)
SELECT * FROM expensive_cte WHERE filter1
UNION ALL
SELECT * FROM expensive_cte WHERE filter2;

If materialized: expensive_cte runs once, results reused (faster)
If inlined: expensive_cte runs twice, once per reference (potentially slower)

Behavior:
- Database-specific (varies by vendor)
- May depend on query complexity
- May depend on cost estimates
- Often not under direct user control

Optimization: Use EXPLAIN or EXPLAIN PLAN to see how your database handles specific CTEs.

