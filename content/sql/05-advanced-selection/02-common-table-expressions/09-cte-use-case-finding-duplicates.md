## CTE Use Case Finding Duplicates

How can CTEs be used to find and investigate duplicate data?

---

Pattern: Use CTE to identify duplicates, then join back to get full details.

Example - Find customers with duplicate emails:
WITH duplicate_emails AS (
  SELECT email
  FROM customer
  GROUP BY email
  HAVING COUNT(*) > 1
)
SELECT c.*
FROM customer c
INNER JOIN duplicate_emails de ON c.email = de.email
ORDER BY c.email, c.customer_id;

How it works:
1. CTE identifies emails that appear more than once
2. Main query joins back to customer table to get full customer records
3. Only customers with duplicate emails appear in results

Benefits:
- Duplicate detection logic is isolated and clear
- Main query is simple: just join and display
- Easy to modify what counts as "duplicate" (e.g., name + email)

Multicolumn duplicates:
WITH duplicate_names AS (
  SELECT first_name, last_name
  FROM customer
  GROUP BY first_name, last_name
  HAVING COUNT(*) > 1
)
SELECT c.*
FROM customer c
JOIN duplicate_names dn ON c.first_name = dn.first_name AND c.last_name = dn.last_name;

