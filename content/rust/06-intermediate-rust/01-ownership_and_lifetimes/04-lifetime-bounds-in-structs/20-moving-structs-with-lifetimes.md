## Moving Structs with Lifetimes

What happens when you move a struct that has lifetime parameters?

---

The struct can be moved normally—moving transfers ownership of the struct itself but doesn't move or copy the referenced data:
```rust
let s = String::from("data");
let holder1 = Holder { data: &s };
let holder2 = holder1;  // Moves holder1
```
After the move, `holder1` is no longer accessible, but `s` is still valid and referenced by `holder2`. The borrow transfers with the struct.

