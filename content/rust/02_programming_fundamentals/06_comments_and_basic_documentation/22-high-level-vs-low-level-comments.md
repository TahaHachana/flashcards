## High-Level vs Low-Level Comments

What's the difference between high-level and low-level comments?

---

High-level comments explain what a section does. Low-level comments explain tricky implementation details.

```rust
// High-level: Parse command line arguments
let args = parse_args();

// Low-level: Use wrapping to handle overflow
let x = a.wrapping_sub(b);
```

