## When NOT To Use CTEs

When should you NOT use CTEs?

---

Don't use CTEs when:

1. Query is simple enough without them
   - SELECT * FROM customer WHERE state = 'CA'
   - Adding CTE would just add complexity

2. Need results across multiple separate queries
   - CTEs have statement scope (one query only)
   - Use temporary tables for multi-query workflows

3. Need to index intermediate results
   - CTEs cannot be indexed
   - Use temporary tables for large intermediate datasets

4. Writing one-time exploratory query
   - Quick ad-hoc analysis doesn't need full documentation
   - Subqueries might be faster to write

5. CTE would just wrap a table with no transformation
   - WITH all_customers AS (SELECT * FROM customer)
   - Serves no purpose, just adds syntax

6. Performance is critical and CTE prevents optimization
   - Profile first, optimize if proven necessary
   - Consider if CTE prevents index usage or predicate pushdown

7. Simple subquery is clearer in context
   - WHERE customer_id = (SELECT MAX(customer_id) FROM customer)
   - Inline subquery is clear enough

General principle: Use CTEs when they improve comprehension or enable functionality (like recursion). Don't use them just because they exist. The goal is readable, maintainable code - not using every feature available.

