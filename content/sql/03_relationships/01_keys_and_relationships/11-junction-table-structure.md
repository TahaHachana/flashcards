## Junction Table Structure

Show the structure of a junction table for Students and Courses. What columns does it have?

---

```
Students:
student_id (PK) | name
1               | John
2               | Jane

Courses:
course_id (PK) | course_name
101            | Math
102            | English

Enrollments (junction table):
enrollment_id (PK) | student_id (FK) | course_id (FK)
1                  | 1               | 101
2                  | 1               | 102
3                  | 2               | 101
```

Junction table has:
1. Its own primary key (optional but recommended)
2. Foreign key to Students
3. Foreign key to Courses

Each row = one student taking one course.

