## Constants Must Be Compile-Time

Can constants be assigned runtime values?

---

No. Constants must be compile-time constant expressions. They cannot be the result of function calls or runtime computations.

```rust
const MAX_SIZE: usize = 1000;              // ✅ OK
const RESULT: u32 = 60 * 60 * 24;         // ✅ OK
const TIME: u64 = get_timestamp();         // ❌ Error
```

