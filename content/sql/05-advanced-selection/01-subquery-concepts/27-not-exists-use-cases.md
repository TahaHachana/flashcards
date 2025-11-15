## NOT EXISTS Use Cases

What are common use cases for the NOT EXISTS operator? Provide an example.

---

Common use cases:
- Finding records without related records
- Implementing "set difference" operations (find A that are not in B)
- More reliable than NOT IN when NULLs might be present

Example - Find actors who never appeared in R-rated films:
SELECT a.first_name, a.last_name
FROM actor a
WHERE NOT EXISTS
  (SELECT 1 FROM film_actor fa
   JOIN film f ON f.film_id = fa.film_id
   WHERE fa.actor_id = a.actor_id AND f.rating = 'R');

For each actor, checks: Are there any R-rated films they appeared in?
- Zero rows → NOT EXISTS is TRUE → include actor
- Any rows → NOT EXISTS is FALSE → exclude actor

