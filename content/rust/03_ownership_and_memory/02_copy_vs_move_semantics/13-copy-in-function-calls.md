## Copy in Function Calls

What happens when you pass a Copy type to a function?

---

The value is copied. The original remains valid after the call.

```rust
fn use_num(n: i32) { }
let num = 42;
use_num(num);
println!("{}", num);  // ✅ Still valid
```

