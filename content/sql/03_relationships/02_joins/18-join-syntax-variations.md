## JOIN Syntax Variations

What are the two main syntax styles for writing JOINs, and which is recommended?

---

1. Explicit JOIN syntax (recommended): Uses JOIN keywords with ON clauses, like `FROM table1 JOIN table2 ON condition`
2. Implicit JOIN syntax (older): Uses comma-separated tables with WHERE conditions, like `FROM table1, table2 WHERE condition`

The explicit syntax is recommended because it's clearer, separates JOIN logic from filtering logic, and is the modern SQL standard.

