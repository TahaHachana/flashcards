## Subqueries In UPDATE Statements

How are subqueries used in UPDATE statements, and what common protection should you include?

---

Used to update columns based on calculated values from other tables.

Example:
UPDATE customer c
SET c.last_update = (SELECT MAX(rental_date) FROM rental r WHERE r.customer_id = c.customer_id)
WHERE EXISTS (SELECT 1 FROM rental r WHERE r.customer_id = c.customer_id);

Protection: The WHERE EXISTS clause prevents setting values to NULL when the subquery returns no rows (e.g., customers with no rentals).

Without WHERE EXISTS, customers with no rentals would get last_update set to NULL.

