## What Is A Subquery?

What is a subquery in SQL, and what are its core characteristics?

---

A subquery is a query contained within another SQL statement. Core characteristics:
- Always enclosed in parentheses ()
- Usually executed before the containing statement
- Returns a temporary result set with statement scope (data discarded after query completes)
- Acts like a temporary table that exists only during query execution
- Can return different "shapes": single value, single column with multiple rows, or multiple columns with multiple rows

Mental model: A preliminary question that gets information needed to answer the main question.

