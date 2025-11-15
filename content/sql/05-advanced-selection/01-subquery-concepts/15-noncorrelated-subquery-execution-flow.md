## Noncorrelated Subquery Execution Flow

Describe the execution flow of a noncorrelated subquery with a concrete example.

---

Example query:
SELECT customer_id, first_name, last_name
FROM customer
WHERE customer_id = (SELECT MAX(customer_id) FROM customer);

Execution flow:
1. Inner query runs once: SELECT MAX(customer_id) FROM customer → returns 599
2. Result (599) replaces the subquery in the outer query
3. Outer query runs once: WHERE customer_id = 599
4. Final result is retrieved

Total executions: Inner query (1x) + Outer query (1x)

