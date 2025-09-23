## Strings

What are the two main string types in Rust?

---

* `&str`: immutable string slice, borrowed view into UTF-8 data.
* `String`: growable, heap-allocated, owned string.

Example:

```rust
let s: &str = "hello";
let mut t: String = String::from("world");
```

