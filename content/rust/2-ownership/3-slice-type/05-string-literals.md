## String Literals

What type are string literals in Rust?

---

String literals have type `&str`, which is a string slice pointing to data baked into the program binary.

```rust
let s: &str = "Hello, world!";
```

