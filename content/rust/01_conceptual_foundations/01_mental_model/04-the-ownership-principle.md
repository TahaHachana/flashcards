## The Ownership Principle

What is the core principle of Rust's ownership system?

---

Every value has exactly one owner at any given time. This single rule, enforced by the compiler, prevents entire categories of bugs including use-after-free, double-free, memory leaks, and data races.

