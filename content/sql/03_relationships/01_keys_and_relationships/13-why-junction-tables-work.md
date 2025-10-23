## Why Junction Tables Work

Explain why junction tables solve the many-to-many problem. What problems do they fix?

---

Problems solved:

1. No repeated data
   - Student info stored once
   - Course info stored once

2. Unlimited connections
   - Add as many rows as needed
   - No fixed limit

3. Easy queries
   - Find all courses for a student: filter by student_id
   - Find all students in a course: filter by course_id

4. Flexible
   - Add/remove connections without changing table structure
   - Can add extra info (enrollment_date, grade)

How it works:
- Breaks many-to-many into TWO one-to-many relationships
- Students → Enrollments (one-to-many)
- Courses → Enrollments (one-to-many)

