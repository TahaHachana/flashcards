## JOIN Order and Performance

Does the order of tables in JOIN clauses affect query results or performance?

---

For INNER JOINs, the order doesn't affect the logical result set (though it may affect column order in SELECT *). For OUTER JOINs, order matters because it determines which table's rows are preserved. For performance, modern query optimizers typically rearrange JOINs for efficiency regardless of how you write them, though starting with smaller tables or more selective filters can sometimes help the optimizer.

