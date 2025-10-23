## Reading Junction Table Data

Given this junction table data, answer: What courses is John taking? What students are in Math?
```
Enrollments:
1 | student:1(John) | course:101(Math)
2 | student:1(John) | course:102(English)
3 | student:2(Jane) | course:101(Math)
```

---

What courses is John (student 1) taking?
- Look for rows with student_id = 1
- Rows 1 and 2
- Courses: 101 (Math), 102 (English)

What students are in Math (course 101)?
- Look for rows with course_id = 101
- Rows 1 and 3
- Students: 1 (John), 2 (Jane)

Mental model: Junction table is a list of connections.
- Row 1: "John is taking Math"
- Row 2: "John is taking English"  
- Row 3: "Jane is taking Math"

Can query in both directions!

