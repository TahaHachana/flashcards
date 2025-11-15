## ALL Operator Mechanics

How does the ALL operator work with subqueries, and what do different comparison operators mean with ALL?

---

ALL: Compare a value to every value in the set. Condition must be true for ALL members.

Comparison operators with ALL:
- > ALL (subquery) = greater than the maximum value
- < ALL (subquery) = less than the minimum value
- = ALL (subquery) = equal to all values (only true if one distinct value)
- <> ALL (subquery) = not equal to any value (equivalent to NOT IN)

Example:
HAVING COUNT(*) > ALL (SELECT COUNT(*) FROM ... GROUP BY ...)

If subquery returns [25, 30, 28, 33], the condition checks:
Is count > 25 AND > 30 AND > 28 AND > 33? (Must exceed all values)

