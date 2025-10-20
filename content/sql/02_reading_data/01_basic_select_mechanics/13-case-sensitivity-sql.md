## Case Sensitivity in SQL

What SQL elements are case-sensitive and which are case-insensitive?

---

Case-insensitive:
- SQL keywords: SELECT, FROM, WHERE (can write select, from, where)
- Column names: FirstName = firstname (usually)
- Table names: Customers = customers (usually)

Case-sensitive:
- String values: 'John' ≠ 'john' ≠ 'JOHN' (ALWAYS)

Convention: 
- Write keywords in UPPERCASE for readability (optional with syntax highlighting)
- Consistent casing for column/table names

Note: Some databases (PostgreSQL with quotes) can be case-sensitive for identifiers, but most treat them as case-insensitive.

