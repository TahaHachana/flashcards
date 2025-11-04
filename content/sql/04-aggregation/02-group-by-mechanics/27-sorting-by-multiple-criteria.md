## Sorting by Multiple Criteria

How can you sort grouped results by multiple criteria, such as first by state alphabetically and then by customer count descending within each state?

---

Use multiple columns in ORDER BY: SELECT state, COUNT(*) AS num_customers FROM customers GROUP BY state ORDER BY state, num_customers DESC. This first sorts by state alphabetically, and within each state value, sorts by customer count in descending order. You can mix ascending and descending as needed for different columns.

