## NULL Handling Rule

What is the core rule for how aggregate functions handle NULL values?

---

All aggregate functions except COUNT(*) completely ignore NULL values - they act as if the NULLs don't exist. COUNT(*) is the exception because it counts rows, not values. For example, with values {1, 3, 5, NULL}, COUNT(*) returns 4, but COUNT(val), SUM(val), AVG(val), MIN(val), and MAX(val) all operate only on {1, 3, 5}.

