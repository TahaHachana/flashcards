## Subqueries In WHERE Clause

What is the most common use of subqueries in the WHERE clause? Provide an example.

---

Most common use: Filter rows based on calculated values or values from other tables.

Example - Find customers who rented exactly 20 films:
SELECT first_name, last_name
FROM customer c
WHERE 20 = (SELECT COUNT(*) 
            FROM rental r 
            WHERE r.customer_id = c.customer_id);

The subquery calculates a value (rental count) for each customer, and the WHERE clause uses that value to filter.

