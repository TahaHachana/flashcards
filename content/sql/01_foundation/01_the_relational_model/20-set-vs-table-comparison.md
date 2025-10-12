## Set vs Table Comparison

Compare a mathematical set to a database table, identifying the key similarities.

---

Similarities:

1. No duplicates
   - Set: Each element appears once
   - Table: Each row is unique (enforced by primary key)

2. No inherent order
   - Set: Elements have no sequence
   - Table: Rows have no guaranteed order (must use ORDER BY)

3. Well-defined membership
   - Set: Clear rules for what belongs
   - Table: Schema and constraints define valid rows

This is why tables can be analyzed using set theory and why set operations (UNION, INTERSECT) work on query results.

