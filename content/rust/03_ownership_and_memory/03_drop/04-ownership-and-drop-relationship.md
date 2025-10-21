## Ownership and Drop Relationship

How does ownership determine when drop is called?

---

Each value has one owner. When the owner goes out of scope, drop is called. Only one owner means drop is called exactly once, preventing leaks and double-frees.

