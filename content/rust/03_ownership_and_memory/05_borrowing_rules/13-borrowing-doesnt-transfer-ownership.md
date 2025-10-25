## Borrowing Doesn't Transfer Ownership

Does borrowing transfer ownership?

---

No. Ownership remains with the original owner. The function just borrows temporarily.

```rust
fn use_str(s: &String) { }
let s = String::from("hello");
use_str(&s);  // Borrow
println!("{}", s);  // ✅ Still valid
```

