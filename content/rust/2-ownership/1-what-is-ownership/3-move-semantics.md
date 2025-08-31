# Move Semantics

What happens when you assign a non-`Copy` type (e.g., `String`) to another variable?

---

Rust moves ownership: the pointer, length, and capacity are copied, but the heap data isn’t. The original binding becomes invalid.

```rust
let s1 = String::from("hello");
let s2 = s1;       // s1 is moved → invalid
// println!("{}", s1); // ERROR: use of moved value
```