## Connection to Ownership

How do structs with lifetime parameters relate to Rust's ownership system?

---

They're a hybrid: they don't own the referenced data (borrowing), but they control when borrowed data must remain valid (lifetime constraint). The referenced data has a separate owner. Example:
```rust
let owner = String::from("data");      // owner owns
let holder = Holder { ref: &owner };   // holder borrows
```
Both must coordinate—the owner must outlive the holder.

