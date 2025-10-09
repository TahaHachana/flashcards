## Expression-Oriented Design

What does it mean that Rust is expression-oriented?

---

Almost everything returns a value: `if/else` expressions, blocks, and match arms all return values. This enables more concise, functional-style code.

```rust
let result = if x > 0 { "positive" } else { "non-positive" };
```

