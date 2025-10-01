## Declaring Constants

How do you declare a constant in Rust, and what rules apply?

---

Use the `const` keyword.
Rules:

* Always immutable (cannot use `mut`).
* Must include a type annotation.
* Value must be a compile-time constant expression.
* Naming convention: UPPERCASE with underscores.

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

