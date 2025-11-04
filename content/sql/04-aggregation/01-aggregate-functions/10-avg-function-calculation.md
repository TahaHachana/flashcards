## AVG Function Calculation

How does the AVG() function calculate the average, and how does it handle NULL values?

---

AVG() calculates the arithmetic mean using the formula: SUM(column) / COUNT(column). It ignores NULL values completely - they are excluded from both the sum and the count. So with values {10, 20, 30, NULL}, AVG returns 20 (which is 60/3), not 15 (which would be 60/4).

