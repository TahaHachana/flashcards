## Subquery Data Fabrication

How can subqueries be used for "data fabrication" - generating data that doesn't exist in the database?

---

Subqueries can generate data on-the-fly that doesn't exist in any table, useful for creating categories, ranges, or synthetic data.

Example - Creating customer payment groups:
FROM (
  SELECT 'Small Fry' level, 0 min, 74.99 max
  UNION ALL
  SELECT 'Average Joes' level, 75 min, 149.99 max
  UNION ALL
  SELECT 'Heavy Hitters' level, 150 min, 9999999.99 max
) groups

This fabricated subquery creates three groups not stored anywhere. You can then JOIN this to actual customer data:

SELECT c.first_name, g.level
FROM customer c
JOIN payment_totals pt ON c.customer_id = pt.customer_id
JOIN groups g ON pt.total BETWEEN g.min AND g.max;

Use cases:
- Binning/categorizing continuous data
- Creating lookup tables without permanent storage
- Generating test data or ranges
- Building reporting categories

