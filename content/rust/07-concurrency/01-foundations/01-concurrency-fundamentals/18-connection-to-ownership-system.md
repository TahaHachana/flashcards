## Connection to Ownership System

How is concurrency safety in Rust connected to the ownership and borrowing system?

---

Concurrency safety is a direct extension of ownership rules. The same rules that prevent use-after-free and double-free also prevent data races: ownership prevents multiple threads from owning the same data, borrowing rules (one mutable or many immutable) prevent concurrent mutation, and lifetimes ensure references don't outlive their data even across threads. It's the same system, just extended to concurrent contexts via Send and Sync traits.

