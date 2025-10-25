## When Interior Mutability Needed

When is interior mutability needed?

---

Rare cases: reference-counted data needing mutation, scenarios where borrow checker is too conservative, or implementing certain data structures. Trade-off: runtime checks vs compile-time guarantees.

