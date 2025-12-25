## Ownership and Data Races

How do Rust's ownership rules prevent data races?

---

Rust's ownership rules prevent data races by ensuring: (1) Each value has one owner - can't have data races if only one thread owns the data, (2) References must be valid - can't have dangling pointers in threads, and (3) One mutable or many immutable references - can't have data races if this rule holds across threads. The compiler enforces these rules even across thread boundaries.

