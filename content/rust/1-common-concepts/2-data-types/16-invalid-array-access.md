# Invalid Array Access

What happens when you try to access an array element with an invalid index?

---

Rust will panic at runtime. For example:
```rust
let a = [1, 2, 3];
let element = a[10]; // This will panic!
```
This is Rust's memory safety in action - it won't allow invalid memory access.