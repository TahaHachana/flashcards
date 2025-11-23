## CTE Versus Subquery In FROM Clause

What are the key differences between CTEs and subqueries in the FROM clause, and when should you use each?

---

Subquery in FROM (derived table):
- Defined inline where used
- Anonymous (no reusable name)
- Can only be referenced once
- Scope limited to defining query

CTE:
- Defined at top of query
- Has descriptive name
- Can be referenced multiple times
- Makes main query cleaner

Use subquery in FROM when:
- Subquery is simple and used only once
- Writing quick, one-off query
- Inline context makes it clearer

Use CTE when:
- Query is complex or used multiple times
- Want to make query more readable
- Building results step-by-step (chaining CTEs)
- Need to explain/maintain the query
- Need to test/debug intermediate results

General principle: If readability matters (production code, shared queries, complex logic), use CTEs. If brevity matters (quick ad-hoc queries), use subqueries.

