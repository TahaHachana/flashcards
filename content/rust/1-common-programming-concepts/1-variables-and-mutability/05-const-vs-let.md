## Const Vs Let

What are the key differences between `const` and `let` in Rust?

---

* `const` is always immutable and cannot be shadowed.
* `const` requires a type annotation and compile-time constant expression.
* `let` can create mutable or immutable variables.
* `let` bindings can be shadowed.

```rust
const MAX_POINTS: u32 = 100_000;
let points = 50; // can shadow later
```

