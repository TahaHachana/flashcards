## Move in Function Calls

What happens when you pass a non-Copy type to a function?

---

Ownership moves to the function. The original becomes invalid.

```rust
fn use_str(s: String) { }
let text = String::from("hello");
use_str(text);
println!("{}", text);  // ❌ Error: text moved
```

