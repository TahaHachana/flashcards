## Constant Folding

What is constant folding and how does it optimize code?

---

Constant folding computes compile-time expressions during compilation, not runtime. This reduces runtime work.

```rust
const SECONDS_PER_DAY: u32 = 60 * 60 * 24;
// Computed at compile time: 86400
```

