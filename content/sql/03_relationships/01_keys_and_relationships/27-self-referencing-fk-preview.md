## Self-Referencing Foreign Key Preview

Can a foreign key reference the same table it's in? Give an example scenario.

---

Yes! Called a self-referencing foreign key or self-join.

Example - Employees with managers:
```
Employees:
employee_id (PK) | name     | manager_id (FK)
1                | Alice    | NULL           (CEO, no manager)
2                | Bob      | 1              (reports to Alice)
3                | Carol    | 1              (reports to Alice)
4                | David    | 2              (reports to Bob)
```

manager_id is a foreign key that references employee_id in the SAME table.

Reading it:
- Bob's manager is employee 1 (Alice)
- Carol's manager is employee 1 (Alice)
- David's manager is employee 2 (Bob)

Other examples:
- Categories with parent categories
- Comments with parent comments (replies)
- Forum threads with parent posts

Covered in detail in Phase 3.3 (Self-joins).

