## Subqueries In DELETE Statements

How are subqueries used in DELETE statements, and what MySQL-specific restriction exists?

---

Used to delete rows based on conditions calculated from related data.

Example - Delete customers who haven't rented in over a year:
DELETE FROM customer
WHERE 365 < ALL (SELECT DATEDIFF(NOW(), rental_date) FROM rental r 
                 WHERE r.customer_id = customer.customer_id);

MySQL restriction: When using correlated subqueries with DELETE, table aliases are not allowed in the DELETE clause itself (though you can use the full table name in the subquery).

