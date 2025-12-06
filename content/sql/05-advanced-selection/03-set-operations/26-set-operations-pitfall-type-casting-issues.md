## Set Operations Pitfall Type Casting Issues

What type casting issues can occur in set operations, and how should you handle them?

---

Problem: Implicit type casting can produce unexpected or invalid results.

Problematic example:
SELECT customer_id FROM customer  -- INT
UNION
SELECT email FROM customer;  -- VARCHAR

Database-specific behavior:
- Some databases allow this, converting INT to VARCHAR
- Result: '123' (as string) mixed with 'email@example.com'
- Probably not what you intended!

Why dangerous:
- May work in one database, fail in another
- Silent conversion may hide logic errors
- Result type may not be what you expect

Correct approach - Explicit casting:
SELECT CAST(customer_id AS VARCHAR(50)) FROM customer
UNION
SELECT email FROM customer;

Best practices:

1. Always ensure compatible types explicitly
2. Use CAST() to make conversions clear
3. Consider if the combination even makes logical sense
4. Document why you're mixing types if intentional

Prevention:
- Review column types before writing set operation
- Think: "Does it make sense to stack these values?"
- Test with sample data to catch type issues early

Key insight: Explicit is better than implicit. Don't rely on database auto-conversion.

