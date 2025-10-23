## Junction Table Definition

What is a junction table? What other names is it known by?

---

Junction table: A table that sits between two tables to create a many-to-many relationship.

Also called:
- Join table
- Bridge table
- Associative entity
- Link table
- Intersection table

Structure:
- Has foreign keys to BOTH tables
- Each row represents ONE connection
- Breaks many-to-many into TWO one-to-many relationships

Example:
```
Students ←→ Enrollments ←→ Courses
(one-to-many)   (many-to-one)
```

The junction table connects the two sides.

