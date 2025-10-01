## Borrow Checker

What role does the borrow checker play in Rust?

---

The borrow checker enforces ownership and borrowing rules at **compile time**, ensuring:

* No dangling references.
* No simultaneous mutable/immutable conflicts.
* No data races.
  This gives memory safety with zero runtime cost.

