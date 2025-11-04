## NULL Impact on AVG

Given a table with salary values {40000, 60000, 80000, NULL}, what will AVG(salary) return and why?

---

AVG(salary) will return 60000, which is (40000 + 60000 + 80000) / 3. The NULL is completely ignored - it's not included in the sum and not included in the count. If you wanted to treat NULL as zero, you would need to use AVG(COALESCE(salary, 0)), which would return 45000 (180000 / 4).

