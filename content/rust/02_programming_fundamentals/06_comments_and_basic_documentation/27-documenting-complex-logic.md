## Documenting Complex Logic

When should you comment complex logic?

---

When the implementation isn't obvious or uses a non-trivial algorithm. Explain the approach or formula used.

```rust
// Calculate using formula: A = P(1 + r)^t
let amount = principal * (1.0 + rate).powf(years);
```

