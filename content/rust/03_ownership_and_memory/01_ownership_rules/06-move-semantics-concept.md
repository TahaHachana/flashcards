## Move Semantics Concept

What is move semantics and why does it exist?

---

When assigning heap-allocated values, ownership transfers instead of copying. This avoids expensive deep copies and prevents double-free by invalidating the old owner.

