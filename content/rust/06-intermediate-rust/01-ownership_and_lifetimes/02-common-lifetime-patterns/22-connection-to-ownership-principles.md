## Connection to Ownership Principles

How do lifetime patterns reflect Rust's ownership principles?

---

Each pattern reflects ownership semantics:
- Patterns 1-2: Borrowing portions of owned data
- Pattern 3: Methods borrowing from `self` (the owner)
- Pattern 4: Distinguishing between borrowed inputs and side effects
- Pattern 5: Temporary borrows that don't escape the function
Lifetimes ensure borrowed data remains valid, while ownership determines who is responsible for cleanup.

