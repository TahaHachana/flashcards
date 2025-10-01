## References Concept

What does the `&` operator do in Rust?

---

It creates a **reference**, allowing access to a value without taking ownership.

```rust
let s1 = String::from("hello");
let len = calculate_length(&s1); // borrow s1
```

