## CTE Versus Subquery When To Use Each

Summarize when to use CTEs versus subqueries (in any clause).

---

Use CTEs when:
- Complex query needs breaking into logical steps
- Same intermediate result used multiple times
- Query needs to be understood by others (or future you)
- Building results progressively (chaining)
- Working with hierarchical data (recursive CTEs)
- Query will be maintained long-term

Use subqueries when:
- Query is simple enough without CTEs
- Subquery used only once
- Writing quick, one-off query
- Inline context makes intent clearer
- Performance is critical and inlining helps

CTE advantages:
- Named intermediate results (documentation)
- Top-to-bottom readability
- Easy to test/debug each step
- Can reference multiple times without duplication
- Enables recursive queries

Subquery advantages:
- Concise for simple cases
- Can appear anywhere an expression is valid
- Sometimes necessary (correlated subqueries in WHERE)
- Less syntax overhead

Rule of thumb: If the query will be read by others or maintained, prefer CTEs. If it's a quick throwaway query, subqueries are fine.

