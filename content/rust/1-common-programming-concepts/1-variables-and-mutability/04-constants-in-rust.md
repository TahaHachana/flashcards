## Constants In Rust

How do constants differ from immutable variables in Rust?

---

* Declared with `const`, never with `mut`.
* Always immutable.
* Must have an explicit type annotation.
* Can be declared in any scope, including global.
* Value must be a compile-time constant expression.
* Unlike `static`, `const` values have no fixed memory address and are inlined wherever used.

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

