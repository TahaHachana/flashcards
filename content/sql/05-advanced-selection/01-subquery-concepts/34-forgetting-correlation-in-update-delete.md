## Forgetting Correlation In UPDATE DELETE

What is a common mistake when using subqueries in UPDATE statements, and how do you fix it?

---

Common mistake: Forgetting to correlate the subquery, which updates all rows to the same value.

Wrong - Updates ALL customers to the same date:
UPDATE customer
SET last_update = (SELECT MAX(rental_date) FROM rental);
-- Every customer gets the same global maximum

Correct - Correlates to update each customer individually:
UPDATE customer c
SET last_update = 
  (SELECT MAX(rental_date) FROM rental r 
   WHERE r.customer_id = c.customer_id);
-- Each customer gets their own maximum

Key difference: The WHERE clause in the subquery correlates it to the outer query, making it calculate per-row instead of globally.

Always consider: Should this calculation be per-row (correlated) or global (noncorrelated)?

