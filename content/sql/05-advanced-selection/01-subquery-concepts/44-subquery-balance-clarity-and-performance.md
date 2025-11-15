## Subquery Balance Clarity And Performance

How should you balance clarity and performance when deciding between subqueries and other approaches?

---

Guiding principle: Clarity matters, but measure before optimizing.

When clarity wins:
- A clear subquery that's 10% slower than a complex JOIN is usually worth it
- Readable code is maintainable code
- Premature optimization wastes time

When performance wins:
- Critical production queries with large datasets
- Queries running frequently (thousands of times per day)
- Correlated subqueries on large tables causing timeouts

Approach:
1. Write it clearly first (often with subqueries)
2. Test with realistic data volumes
3. Only optimize if there's a proven performance problem
4. Profile to find the actual bottleneck (might not be the subquery!)
5. Document any performance-driven complexity

Example: Correlated subquery in SELECT clause might be 5x slower than JOIN, but if query takes 50ms vs 10ms and runs once per hour, the clarity is worth it.

