## Set Operations Use Case Finding Overlaps

How do you use INTERSECT to find overlapping data between tables for validation purposes?

---

Use case: Find records that appear in multiple places (data validation, finding dual roles).

Example - Find names in both customers and employees:
SELECT first_name, last_name FROM customer
INTERSECT
SELECT first_name, last_name FROM employee;

Result: Names that exist in both tables (potential dual-role people).

Important limitation: Matching by name alone isn't definitive - they could be different people with the same name. Better to match on unique identifiers (IDs, email) if available.

Improved version with IDs:
SELECT customer_id FROM customer
INTERSECT
SELECT employee_id FROM employee_customer_map;

Use cases:
- Finding people with multiple roles
- Verifying data synchronization between systems
- Identifying duplicate records across tables
- Quality checks ("these should/shouldn't overlap")

Key insight: INTERSECT answers "what's in both?" - useful for validation and finding relationships between datasets.

