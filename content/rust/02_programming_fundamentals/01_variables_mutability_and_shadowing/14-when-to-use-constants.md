## When to Use Constants

When should you use constants instead of variables?

---

For fixed values known at compile time, values used throughout your program, configuration values that never change, and meaningful names for magic numbers.

```rust
const MAX_RETRIES: u32 = 3;
const TIMEOUT_MS: u64 = 5000;
```

