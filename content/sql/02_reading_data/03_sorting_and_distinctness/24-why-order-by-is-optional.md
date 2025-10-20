## Why ORDER BY Is Optional

Why is ORDER BY optional in SQL? When should you use it?

---

ORDER BY is optional because:
- Sometimes order doesn't matter
- Sorting can be expensive for large result sets
- Application might sort after retrieval
- Database makes no promises without it

When you SHOULD use ORDER BY:
- Results displayed to users
- Order matters for business logic
- Selecting top/bottom N records
- Comparing sequences
- Generating reports
- Pagination

When you CAN skip ORDER BY:
- Order genuinely doesn't matter
- Application will re-sort results
- Performance critical and order unnecessary
- Internal processing only

Key principle: Never ASSUME order without ORDER BY, even if it seems consistent. Database makes no promises without explicit ORDER BY clause.

