## Tables Have No Inherent Order

Why can't you rely on the order of rows without an ORDER BY clause?

---

Tables are sets, and sets have no inherent order (from set theory).

This means:
- Rows have no guaranteed sequence
- Order might seem consistent but is not promised
- Physical storage order can change as database optimizes
- Without ORDER BY, database can return rows in any sequence

Example:
```sql
SELECT * FROM customers;
```

Might return rows in insertion order today, but differently tomorrow after database maintenance.

Mental model: Rows are like balls in a bag - there's no inherent "first" or "last" until you arrange them.

ORDER BY is the ONLY way to guarantee order.

