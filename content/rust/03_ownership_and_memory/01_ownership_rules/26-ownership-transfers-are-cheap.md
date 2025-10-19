## Ownership Transfers Are Cheap

What is the performance cost of moving ownership?

---

Essentially free - just invalidates the old variable. No data is copied. The heap allocation stays in place, only ownership tracking changes.

