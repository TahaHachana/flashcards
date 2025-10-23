## Automatic Dereferencing

When does Rust automatically dereference?

---

For method calls. You don't need * for methods.

```rust
let s = String::from("hello");
let r = &s;
println!("{}", r.len());  // Automatic
```

