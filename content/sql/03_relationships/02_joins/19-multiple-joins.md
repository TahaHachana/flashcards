## Multiple JOINs

How do you join three or more tables together, and in what order are the JOINs processed?

---

Chain multiple JOINs together sequentially. JOINs are processed left-to-right: the first JOIN combines the first two tables, then the result is joined with the third table, and so on. Each JOIN operation builds on the result of the previous one.

