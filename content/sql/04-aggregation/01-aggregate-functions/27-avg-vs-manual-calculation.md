## AVG vs Manual Calculation

What's wrong with calculating average as SUM(column) / COUNT(*) instead of using AVG(column)?

---

SUM(column) / COUNT(*) includes NULL values in the denominator (counting rows), while AVG(column) excludes NULLs from both numerator and denominator. With values {10, 20, 30, NULL}, AVG(column) correctly returns 20 (60/3), but SUM(column)/COUNT(*) returns 15 (60/4). Use AVG() unless you specifically want to treat missing values as zeros.

