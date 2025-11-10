## Efficiency of WHERE vs HAVING

Why is using WHERE more efficient than HAVING for non-aggregate conditions?

---

WHERE filters rows before the expensive grouping operation, reducing the amount of data that needs to be grouped. Example: WHERE customer_id IN (1,2,3) filters to 3 customers first, then groups only those rows. Using HAVING customer_id IN (1,2,3) groups all customers (thousands), then filters to 3. WHERE reduces work, HAVING does unnecessary work on data that will be filtered out.

