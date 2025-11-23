## CTE Use Case Simplifying Aggregation Then Joining

How do CTEs simplify the pattern of "aggregate first, then join to other tables"?

---

Problem: Mixing aggregation with joins creates complex queries.

Without CTE (messy):
SELECT c.first_name, c.last_name, ct.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
WHERE 20 = (SELECT COUNT(*) FROM rental r WHERE r.customer_id = c.customer_id);
-- Correlated subquery runs once per customer

With CTE (clean):
WITH customer_rental_counts AS (
  SELECT customer_id, COUNT(*) as rental_count
  FROM rental
  GROUP BY customer_id
)
SELECT c.first_name, c.last_name, ct.city, crc.rental_count
FROM customer_rental_counts crc
JOIN customer c ON crc.customer_id = c.customer_id
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
WHERE crc.rental_count = 20;

Benefits:
- Aggregation logic isolated in CTE
- Main query focuses on joining tables
- Aggregation runs once, not once per row
- Can reuse rental counts if needed elsewhere

