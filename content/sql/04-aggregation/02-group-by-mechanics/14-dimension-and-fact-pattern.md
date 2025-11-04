## Dimension and Fact Pattern

What is the common pattern when grouping with dimension and fact tables?

---

Pattern: Group by columns from dimension tables (descriptive data like customers, products, stores) and aggregate columns from fact tables (transactional data like orders, sales). Example: GROUP BY customers.customer_id (dimension) with SUM(orders.amount) (fact aggregation). This shows statistics about the dimensions using data from the facts.

