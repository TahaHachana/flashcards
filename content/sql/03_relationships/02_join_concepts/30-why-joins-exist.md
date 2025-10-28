## Why JOINs Exist

Why do relational databases use JOINs instead of storing all related data in a single table?

---

JOINs exist because of normalization. Storing data in separate tables eliminates redundancy, maintains data integrity, and makes updates easier. JOINs are the mechanism that temporarily reunites this normalized data when you need to see it together. They allow you to benefit from normalized storage (efficient, consistent) while still being able to view and query related data as if it were in one table.

