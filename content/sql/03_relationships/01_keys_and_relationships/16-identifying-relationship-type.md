## Identifying Relationship Type

What two questions should you ask to identify the relationship type? How do the answers determine the pattern?

---

Questions:
1. Can A have multiple B's?
2. Can B have multiple A's?

Decision tree:

Both YES → Many-to-many (junction table needed)
Example: Students ↔ Courses

One YES, one NO → One-to-many (FK on "many" side)
Example: Customer → Orders

Both NO → One-to-one (rare, might combine into one table)
Example: Person → Passport

Practice:
- Customer/Orders: Customer has many orders? YES. Order has many customers? NO. → One-to-many
- Books/Authors: Book has many authors? YES. Author has many books? YES. → Many-to-many

