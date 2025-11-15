## Subquery Statement Scope Lifecycle

What does "statement scope" mean for subqueries, and what is their lifecycle?

---

Statement scope: Subquery results exist only during the execution of the containing statement, then are immediately discarded.

Lifecycle:
1. Query starts executing
2. Subquery executes and generates temporary result set
3. Result set held in memory
4. Containing statement uses the results
5. Statement completes
6. Server frees memory allocated to subquery results
7. Results are gone - cannot be accessed by subsequent queries

Contrast with:
- Temporary tables: Persist until session ends or explicitly dropped
- Views: Persist in data dictionary until explicitly dropped
- CTEs: Similar statement scope (section 5.2 will cover these)

Mental model: Subqueries are ephemeral helpers that live only as long as the query that needs them.

