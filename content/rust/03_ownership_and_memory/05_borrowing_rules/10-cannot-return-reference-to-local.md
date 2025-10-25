## Cannot Return Reference to Local

Why can't you return a reference to a local variable?

---

Local variable is dropped when function ends, making the reference dangle. Must return owned value instead.

```rust
fn dangle() -> &String {
    let s = String::from("hello");
    &s  // ❌ Error: s dropped, reference invalid
}
```

