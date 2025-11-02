## What Are Lifetimes in Rust?

What are lifetime annotations in Rust, and what problem do they solve?

---

Lifetime annotations are labels that describe the scope during which a reference remains valid. They solve the problem of tracking how long referenced data is valid so the borrow checker can prevent dangling references. Lifetimes don't change how long data lives—they describe relationships between the lifetimes of different references to verify safety at compile time.

