## Subquery Key Conceptual Insights

What are the three most important conceptual insights about subqueries?

---

1. Subqueries are temporary and ephemeral
   - They exist only during query execution, then disappear
   - Think of them as ephemeral helpers that answer preliminary questions
   - Statement scope means: live only as long as the containing query

2. Shape determines usage
   - Single value (scalar) → Use comparison operators (=, <, >)
   - Multiple rows, one column → Use set operators (IN, ALL, ANY, EXISTS)
   - Multiple rows and columns → Use multicolumn IN or join in FROM
   - Mismatch between shape and operator → Error

3. Correlation changes everything
   - Noncorrelated: Run once, result reused (efficient)
   - Correlated: Run once per outer row (potentially expensive)
   - Performance delta can be 100x or more on large datasets
   - Correlation is determined by references to outer query columns

Master these three concepts, and everything else about subqueries follows logically.

