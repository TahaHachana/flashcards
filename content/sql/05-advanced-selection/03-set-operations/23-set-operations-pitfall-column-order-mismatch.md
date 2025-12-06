## Set Operations Pitfall Column Order Mismatch

What is the column order mismatch pitfall, and how do you avoid it?

---

Pitfall: Columns in different order between queries, causing data scrambling.

Problem example:
SELECT first_name, last_name FROM customer
UNION
SELECT last_name, first_name FROM employee;  -- REVERSED!

Result: first_name column contains last names from employees
        last_name column contains first names from employees

Why dangerous:
- Query runs without error
- Data appears valid
- Results are completely wrong
- Hard to detect without careful inspection

How to avoid:

1. Maintain consistent column order:
SELECT first_name, last_name FROM customer
UNION
SELECT first_name, last_name FROM employee;

2. Visually align queries for review:
SELECT first_name,  last_name  FROM customer
UNION
SELECT first_name,  last_name  FROM employee;

3. Use same table aliases/column names when possible

4. Test with known data to verify correctness

5. Add comments documenting column purposes

Prevention mindset: Treat column order as part of the contract between queries. Visual alignment makes mismatches obvious.

