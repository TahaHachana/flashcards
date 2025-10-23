## Junction Table Primary Key Options

What are the two approaches for primary keys in junction tables? What are the pros/cons of each?

---

Option 1: Compound primary key (both FKs)
```
student_id (PK, FK) | course_id (PK, FK)
1                   | 101
1                   | 102
```
Pro: Automatically prevents duplicate enrollments
Con: Compound keys can be awkward to reference

Option 2: Separate surrogate key
```
enrollment_id (PK) | student_id (FK) | course_id (FK)
1                  | 1               | 101
2                  | 1               | 102
```
Pro: Simpler, can reference specific enrollment easily
Con: Need separate UNIQUE constraint to prevent duplicates

Best practice: Use surrogate key (enrollment_id) + UNIQUE constraint on (student_id, course_id).

