## Data Race vs Race Condition

What is the difference between a data race and a race condition? Which does Rust prevent?

---

A data race is unsynchronized concurrent access to memory where at least one is a write - this causes undefined behavior and memory safety issues. A race condition is when program correctness depends on the relative timing of events - this affects program logic but not memory safety. Rust prevents data races at compile time but allows race conditions (which are logic bugs, not safety bugs).

