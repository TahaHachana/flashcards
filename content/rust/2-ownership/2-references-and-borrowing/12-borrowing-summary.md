## Borrowing Summary

Summarize the rules of references and borrowing in Rust.

---

* References (`&`) let you access without ownership.
* Borrowing = using references.
* Multiple immutable borrows are allowed.
* Only one mutable borrow at a time.
* Mutable + immutable borrows cannot coexist.
* Borrow checker enforces safety at compile time.
* Dangling references are not allowed.

