## Set Theory - Unordered Property

In set theory, what is the rule about element order, and how does this apply to database tables?

---

A set has no inherent order - elements have no meaningful sequence.

In databases:
- Rows in a table have no inherent order
- You cannot rely on rows being in any particular sequence
- This is why you must use ORDER BY to guarantee a specific ordering

