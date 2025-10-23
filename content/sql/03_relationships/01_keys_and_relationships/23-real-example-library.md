## Real Example Library

Design a library system with Books, Authors, and Patrons (borrowers). Identify all the many-to-many relationships.

---

Structure:
```
Authors:
author_id (PK) | name

Books:
book_id (PK) | title | isbn

BookAuthors (junction):
book_id (FK) | author_id (FK)

Patrons:
patron_id (PK) | name

Loans (junction):
loan_id (PK) | book_id (FK) | patron_id (FK) | loan_date | return_date
```

Many-to-many relationships:
1. Books ↔ Authors (via BookAuthors)
   - Books can have multiple authors
   - Authors can write multiple books

2. Patrons ↔ Books (via Loans)
   - Patrons can borrow multiple books
   - Books can be borrowed by multiple patrons (over time)

Note: Loans is both a junction table AND has its own data (dates). Very common pattern!

