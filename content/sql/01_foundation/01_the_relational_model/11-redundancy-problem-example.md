## Redundancy Problem Example

Why is data redundancy (storing the same information in multiple places) a problem? Give a concrete example.

---

Example: Storing an author's birth date in every book record

Problems:
1. If the birth date is wrong, you must update hundreds of records
2. Miss one update, and now you have inconsistent data
3. Wastes storage space
4. Which copy is correct when they differ?

Solution: Store author information once, reference it using author_id (foreign key) from books.

