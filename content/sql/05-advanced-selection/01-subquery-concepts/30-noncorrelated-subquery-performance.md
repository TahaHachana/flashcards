## Noncorrelated Subquery Performance

What are the performance characteristics of noncorrelated subqueries?

---

Performance characteristics:

Advantages:
- Generally efficient - execute only once
- Results can be cached and reused by the containing query
- Predictable execution time regardless of outer query size

Cost:
- One-time execution cost of the subquery itself
- Memory to hold results during query execution

Example:
WHERE amount > (SELECT AVG(amount) FROM payment);

Execution: AVG calculation runs once, result cached, then used to filter all rows.

Contrast with correlated: If outer query has 1000 rows and uses a correlated subquery, that subquery runs 1000 times.

