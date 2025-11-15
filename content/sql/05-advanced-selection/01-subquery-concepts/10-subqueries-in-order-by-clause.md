## Subqueries In ORDER BY Clause

How are subqueries used in the ORDER BY clause, and what is their key characteristic?

---

Used to sort by calculated values without showing them in the result set.

Key characteristic: The subquery value is used purely for sorting - it doesn't appear in the output columns.

Example - Sort actors by film count (descending) without showing the count:
SELECT actor_id, first_name, last_name
FROM actor a
ORDER BY (SELECT COUNT(*) FROM film_actor fa WHERE fa.actor_id = a.actor_id) DESC;

The count is calculated for sorting but not displayed.

