## Testing Noncorrelated Subqueries

How can you test and debug a noncorrelated subquery when confused about its behavior?

---

Run the subquery independently (without parentheses) to see what it returns.

Example:
Original query:
WHERE customer_id = (SELECT MAX(customer_id) FROM customer);

Test the subquery alone:
SELECT MAX(customer_id) FROM customer;
-- Returns: 599

Now you understand the outer query is really:
WHERE customer_id = 599;

This technique only works with noncorrelated subqueries (correlated ones need values from the outer query).

