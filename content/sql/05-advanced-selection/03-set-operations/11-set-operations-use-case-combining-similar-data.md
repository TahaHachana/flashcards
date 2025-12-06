## Set Operations Use Case Combining Similar Data

How are set operations used to combine data from similar tables, and when should you add identifying columns?

---

Use case: Combine similar data from multiple sources into one list.

Example - Invite customers and employees to event:
SELECT first_name, last_name, email, 'Customer' AS type
FROM customer
UNION ALL
SELECT first_name, last_name, email, 'Employee' AS type
FROM employee
ORDER BY last_name, first_name;

Why UNION ALL: We want all people, even if some names appear in both tables (they're different people who happen to share names).

Adding type column: The literal 'Customer' and 'Employee' help track the source of each row.

Pattern - Adding identifying columns:
SELECT columns, 'SOURCE_A' AS source FROM table_a
UNION ALL
SELECT columns, 'SOURCE_B' AS source FROM table_b;

Benefit: Helps interpret results, especially when combining similar data from different sources. You can filter, group by, or report on the source.

When to use: Combining contact lists, transaction logs, event data, or any similar structures from multiple tables.

