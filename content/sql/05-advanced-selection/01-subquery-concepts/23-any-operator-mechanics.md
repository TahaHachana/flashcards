## ANY Operator Mechanics

How does the ANY operator work with subqueries, and how does it differ from ALL?

---

ANY: Compare a value to the set. Condition must be true for at least one member.

Comparison operators with ANY:
- > ANY (subquery) = greater than the minimum value
- < ANY (subquery) = less than the maximum value
- = ANY (subquery) = equal to at least one value (equivalent to IN)

Difference from ALL:
- ALL: Must satisfy condition for every member
- ANY: Must satisfy condition for at least one member

Example:
HAVING SUM(amount) > ANY (SELECT SUM(amount) FROM ... GROUP BY ...)

If subquery returns [150, 175, 160], checks:
Is sum > 150 OR > 175 OR > 160? (Must exceed at least one value)

