## CTE Versus Nested Subquery Readability

Why are CTEs more readable than nested subqueries? Explain with an example pattern.

---

Nested subqueries require reading from inside-out (hard):
SELECT ...
FROM (
  SELECT ...
  FROM (SELECT ... FROM ...) inner
  WHERE ...
) outer
WHERE ...;

CTEs enable top-to-bottom reading (natural):
WITH 
  step_one AS (SELECT ... FROM ...),
  step_two AS (SELECT ... FROM step_one WHERE ...),
  step_three AS (SELECT ... FROM step_two)
SELECT ... FROM step_three;

Benefits:
- Descriptive names explain purpose of each step
- Natural reading order matches human thinking
- Easy to test each step independently
- Easy to add comments at each step
- Simple to modify individual steps

Principle: CTEs transform nested puzzles into step-by-step recipes.

