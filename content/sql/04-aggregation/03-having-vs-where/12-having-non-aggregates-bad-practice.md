## HAVING with Non Aggregates Bad Practice

Can you use HAVING with non-aggregate conditions? Should you?

---

Technically yes, you can use HAVING with non-aggregate conditions (like HAVING state = 'CA'), but you shouldn't. Use WHERE instead because it's more efficient - WHERE filters before grouping, while HAVING filters after. Only use HAVING for conditions that genuinely need aggregate functions or must be evaluated after grouping.

