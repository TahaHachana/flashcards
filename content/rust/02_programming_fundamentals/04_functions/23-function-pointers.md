## Function Pointers

Can functions be stored in variables and passed as arguments?

---

Yes. Use function pointers with type fn(params) -> return_type.

```rust
fn add(a: i32, b: i32) -> i32 { a + b }
fn apply(a: i32, b: i32, op: fn(i32, i32) -> i32) -> i32 {
    op(a, b)
}
let result = apply(5, 3, add);  // 8
```

