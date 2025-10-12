## Declarative vs Procedural Querying

What does it mean that SQL is "declarative" rather than "procedural"? Why is this important?

---

Declarative: You describe WHAT you want, not HOW to get it
Procedural: You specify the exact steps to retrieve data

Example:
- Declarative SQL: "SELECT * FROM customers WHERE age > 18"
- Procedural: "Open customers file, read each record, check if age > 18, if yes add to results..."

Importance:
- Simpler for users (don't need to know storage details)
- Database can optimize the "how" automatically
- Same query works even if storage structure changes

