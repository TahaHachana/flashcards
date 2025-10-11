## Type Mismatch in Operations

Can you mix different numeric types in operations?

---

No. You must explicitly convert types using the as keyword.

```rust
let x: i32 = 5;
let y: f64 = 2.5;
let z = x + y;  // ❌ Error

let z = x as f64 + y;  // ✅ OK
```

