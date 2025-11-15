## Correlated Subquery Execution Flow

Describe the execution flow of a correlated subquery and explain the performance implication.

---

Example - Find customers who rented exactly 20 films:
SELECT c.first_name, c.last_name
FROM customer c
WHERE 20 = (SELECT COUNT(*) FROM rental r WHERE r.customer_id = c.customer_id);

Execution flow:
1. Outer query retrieves first customer row (customer_id = 1)
2. Inner query executes: "Count rentals for customer_id = 1"
3. If count = 20, include this customer in results
4. Repeat for customer_id = 2, 3, 4, ... 599

Performance implication: If customer table has 599 rows, the correlated subquery executes 599 times! For large datasets, this can be very slow.

