## Noncorrelated Subquery Definition

What is a noncorrelated subquery, and what are its key characteristics?

---

A noncorrelated subquery is completely self-contained - it doesn't reference anything from the containing query.

Characteristics:
- Can be executed by itself in isolation
- Executed once, before the containing statement runs
- Result is then used by the containing query
- Most subqueries you'll write are noncorrelated
- Generally efficient (execute once, results can be cached)

Example:
WHERE customer_id = (SELECT MAX(customer_id) FROM customer);

The inner query doesn't reference the outer query's customer table.

