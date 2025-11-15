## Multiple-Row Single-Column Subquery

What is a multiple-row, single-column subquery, and what special operators does it require?

---

A subquery that returns multiple values in one column (a list of values).

Requires special set operators:
- IN / NOT IN: Check if value exists in the set
- ALL: Compare to all members (condition must be true for every member)
- ANY: Compare to all members (condition must be true for at least one member)
- EXISTS / NOT EXISTS: Check if subquery returns any rows

Example: (SELECT country_id FROM country WHERE country <> 'India') returns [1, 2, 3, 4, ...]

