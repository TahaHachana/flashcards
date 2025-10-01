## Data Race Conditions

What three conditions define a data race, and how does Rust prevent them?

---

A data race occurs when:

1. Two or more pointers access the same data simultaneously.
2. At least one is writing.
3. No synchronization is used.

Rust prevents this by restricting to one mutable reference or multiple immutable ones.

