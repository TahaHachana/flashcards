## Copy Trait Requirement

What requirement must a type meet to implement Copy?

---

All parts must be on the stack. If any part is on the heap, the type must use move semantics.

