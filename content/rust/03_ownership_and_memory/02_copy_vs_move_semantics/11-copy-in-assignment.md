## Copy in Assignment

What happens when you assign a Copy type to a new variable?

---

The value is duplicated. Both variables are valid and independent.

```rust
let x = 5;
let y = x;
println!("{}, {}", x, y);  // ✅ Both valid
```

