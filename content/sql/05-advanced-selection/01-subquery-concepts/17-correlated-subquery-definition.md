## Correlated Subquery Definition

What is a correlated subquery, and what are its key characteristics?

---

A correlated subquery references one or more columns from the containing query - it's dependent on the outer query for context.

Characteristics:
- Cannot be executed by itself (needs values from outer query)
- Executed once for each row being evaluated by containing query
- Much more computationally expensive than noncorrelated subqueries
- Common in UPDATE and DELETE statements
- Correlation is usually in the WHERE clause of the subquery

Example:
WHERE 20 = (SELECT COUNT(*) FROM rental r WHERE r.customer_id = c.customer_id);
                                                    -- References outer query ↑

