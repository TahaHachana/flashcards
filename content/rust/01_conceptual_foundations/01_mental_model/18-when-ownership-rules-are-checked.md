## When Ownership Rules Are Checked

When are Rust's ownership rules enforced, and what is the performance impact?

---

Ownership rules are checked entirely at compile time, with zero runtime cost. The compiler verifies all safety guarantees before generating machine code, resulting in safe programs with no runtime overhead.

