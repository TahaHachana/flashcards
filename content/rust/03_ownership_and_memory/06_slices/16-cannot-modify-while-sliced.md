## Cannot Modify While Sliced

Can you modify a collection while an immutable slice exists?

---

No. The immutable slice prevents modification.

```rust
let slice = &vec[1..4];
vec.push(6);  // ❌ Error: cannot borrow as mutable
println!("{:?}", slice);
```

