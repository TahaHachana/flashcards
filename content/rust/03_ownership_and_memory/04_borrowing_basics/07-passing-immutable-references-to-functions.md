## Passing Immutable References to Functions

What happens when you pass an immutable reference to a function?

---

The function borrows the data temporarily. When the function ends, the reference goes out of scope but doesn't drop the data. Original remains valid.

```rust
fn use_str(s: &String) { }
let my_str = String::from("hello");
use_str(&my_str);
println!("{}", my_str);  // ✅ Still valid
```

