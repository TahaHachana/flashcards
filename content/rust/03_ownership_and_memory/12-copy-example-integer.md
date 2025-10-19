## Copy Example Integer

What happens when you assign one integer to another?

---

The value is copied. Both variables remain valid because integers are Copy types.

```rust
let x = 5;
let y = x;  // x is still valid
println!("{} {}", x, y);  // ✅ Both work
```

