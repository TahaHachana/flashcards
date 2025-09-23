## Mutable Binding vs Value Mutability

What’s the difference between a mutable binding and value mutability in Rust?

---

* `let mut` makes the **binding** mutable, so you can reassign it or call mutating methods.
* Some types (like `Vec`) are **internally mutable** and support mutation through methods.
* An immutable binding cannot call mutating methods, even if the value type is mutable.

```rust
let v = vec![1, 2, 3];
// v.push(4); // ❌ cannot borrow as mutable

let mut v = vec![1, 2, 3];
v.push(4); // ✅ works
```

