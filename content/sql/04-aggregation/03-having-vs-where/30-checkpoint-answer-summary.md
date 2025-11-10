## Checkpoint Answer Summary

Summarize in 2-3 sentences why you can't use WHERE to filter on COUNT().

---

WHERE is evaluated before GROUP BY and before any aggregate functions are calculated. At the point WHERE runs, groups don't exist yet and COUNT() hasn't been calculated. You're trying to filter on information that doesn't exist yet - it's conceptually impossible to filter on an aggregate value before that value has been computed. Use HAVING instead, which runs after aggregates are calculated.

