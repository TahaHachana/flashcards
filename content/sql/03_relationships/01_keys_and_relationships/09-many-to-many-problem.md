## Many-to-Many Problem

Why can't you represent a many-to-many relationship with just two tables? What goes wrong?

---

Example: Students and Courses
- One student takes many courses
- One course has many students

Can't use single foreign key:

Wrong - Multiple values in one column:
```
Students:
student_id | courses
1          | "Math, English, History"  ← Violates atomicity!
```

Wrong - Multiple foreign key columns:
```
Students:
student_id | course1 | course2 | course3
1          | 101     | 102     | 103     ← Fixed limit, lots of NULLs
```

Problems:
- Can't query efficiently
- Can't find all students in a course
- Violates normalization
- Inflexible

Solution: Junction table needed!

