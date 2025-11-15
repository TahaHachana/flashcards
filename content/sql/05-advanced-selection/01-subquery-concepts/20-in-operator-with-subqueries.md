## IN Operator With Subqueries

How does the IN operator work with subqueries? Provide an example.

---

IN checks if a value exists in a set of values returned by a subquery.

Example - Find films in the 'Action' category:
SELECT title
FROM film
WHERE film_id IN 
  (SELECT fc.film_id 
   FROM film_category fc
   JOIN category c ON fc.category_id = c.category_id
   WHERE c.name = 'Action');

How it works:
1. Subquery returns a list of film_ids: [1, 5, 12, 23, ...]
2. IN operator checks if each film's ID is in that list
3. Films with matching IDs are included in results

