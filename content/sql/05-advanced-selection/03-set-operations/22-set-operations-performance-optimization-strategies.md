## Set Operations Performance Optimization Strategies

What are the main strategies for optimizing set operation performance?

---

Optimization strategies:

1. Use UNION ALL when possible
   - Fastest option, no duplicate checking overhead
   - Default choice unless deduplication required

2. Limit rows before combining
   - Filter in each query before set operation
   - Don't combine everything then filter
   
   Bad: (SELECT * FROM large_table UNION SELECT * FROM large_table) WHERE filter
   Good: SELECT * FROM large_table WHERE filter UNION SELECT * FROM large_table WHERE filter

3. Index appropriately
   - Ensure each individual query is optimized
   - Set operations can only be as fast as their slowest component
   - Add indexes on filter columns used in WHERE clauses

4. Use EXPLAIN/EXPLAIN PLAN
   - Understand how database executes the set operation
   - Look for sequential scans on large tables
   - Check if indexes are being used

5. Consider alternatives for large datasets
   - Temporary tables with indexes (if combining repeatedly)
   - Materialized views (if result reused frequently)
   - Application-level combination (if performance critical)

When set operations are slow:
- Large result sets with UNION (duplicate detection expensive)
- Many operations chained (multiple passes over data)
- Complex subqueries in each part (each executes independently)

Key insight: Optimize each component query first; set operation speed depends on component speed.

