## Set Operations Use Case Finding Missing Data

How do you use EXCEPT to find missing data, and when is it better than a LEFT JOIN?

---

Use case: Find records in one table that don't exist in another (missing data, gaps).

Example - Customers with no purchases:
SELECT customer_id FROM customer
EXCEPT
SELECT customer_id FROM sales;

Result: Customer IDs with no sales records.

Alternative with OUTER JOIN:
SELECT c.customer_id
FROM customer c
LEFT JOIN sales s ON c.customer_id = s.customer_id
WHERE s.customer_id IS NULL;

When to use EXCEPT:
- Only need the IDs (simpler, clearer intent)
- Want to emphasize "set difference" logic
- Result is just a list of missing items

When to use LEFT JOIN:
- Need additional details from the customer table
- Building a more complex query with multiple joins
- Need to count or aggregate the missing items

Key difference: EXCEPT focuses on the difference itself; LEFT JOIN gives you access to full rows for further processing.

Other use cases: Orphaned records, incomplete processes, data quality checks.

