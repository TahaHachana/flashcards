## Subqueries In INSERT Statements

How can subqueries be used in INSERT statements, and what advantage does this provide?

---

Subqueries can look up values dynamically when inserting data.

Advantage: Instead of executing separate queries to find IDs then manually inserting them, you do everything in one statement.

Example - Insert film_actor relationship by looking up IDs from names:
INSERT INTO film_actor (actor_id, film_id, last_update)
VALUES (
  (SELECT actor_id FROM actor WHERE first_name = 'JENNIFER' AND last_name = 'DAVIS'),
  (SELECT film_id FROM film WHERE title = 'ACE GOLDFINGER'),
  NOW()
);

