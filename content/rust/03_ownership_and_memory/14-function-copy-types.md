## Function Copy Types

What happens when you pass a Copy type to a function?

---

The value is copied. The original variable remains valid after the call.

```rust
fn make_copy(x: i32) { }
let num = 42;
make_copy(num);  // num still valid
println!("{}", num);  // ✅ Works
```

