## When To Use Set Operations Over JOINs

When should you use set operations instead of JOINs?

---

Use set operations when:

1. Combining similar data from multiple sources
   - All customers from different regional databases
   - Current + archived sales data
   - Example: SELECT * FROM current_sales UNION ALL SELECT * FROM archived_sales

2. Building union of disparate but structurally similar data
   - Contact list: customers + suppliers + employees
   - All transactions: sales + refunds + adjustments

3. Finding differences or overlaps between datasets
   - INTERSECT: What's in both?
   - EXCEPT: What's in A but not B?
   - Example: SELECT id FROM should_exist EXCEPT SELECT id FROM actually_exists

4. Creating comprehensive views spanning multiple tables
   - All events: user logins + purchases + support tickets
   - Timeline of activities from different sources

Use JOINs when:

1. Need columns from multiple tables in the same row
   - Customer name + order details + product info

2. Working with relationships between tables
   - Orders with their line items
   - Employees with their departments

3. Aggregating across relationships
   - Total sales per customer (JOIN customer to orders)

Key distinction: Set operations answer "stack these together"; JOINs answer "merge these side by side."

