## The Redundant Grouping Pattern

What is the "redundant grouping pattern" and why would you use it?

---

Redundant grouping means grouping by multiple versions of the same underlying data - typically one for display and another for sorting. Example: GROUP BY DAYNAME(date), DAYOFWEEK(date) groups by both the day name ('Monday') and day number (2). This is needed because you can only SELECT or ORDER BY what's in GROUP BY, so if you want to display names but sort by numbers, you must group by both.

