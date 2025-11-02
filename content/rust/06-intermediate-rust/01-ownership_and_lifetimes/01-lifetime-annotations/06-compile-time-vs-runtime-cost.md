## Compile-Time vs Runtime Cost

Do lifetime annotations have any runtime cost or performance impact?

---

No. Lifetimes are entirely a compile-time concept with zero runtime cost. They exist only for borrow checker verification during compilation and are erased before the program runs. This is part of Rust's zero-cost abstractions philosophy.

