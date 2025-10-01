## Move Semantics

What happens when you assign or pass ownership of a value in Rust?

---

Ownership is **moved**.
The original binding becomes invalid to prevent double frees.

```rust
let s1 = String::from("hello");
let s2 = s1; // move
// println!("{s1}"); // ❌ invalid
```

