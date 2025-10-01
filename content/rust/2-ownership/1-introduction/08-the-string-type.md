## The String Type

How does the `String` type demonstrate ownership in Rust?

---

`String` manages heap-allocated, growable text.
It shows how ownership works for dynamically allocated data, with moves, scope-based cleanup, and mutable heap storage.

```rust
let mut s = String::from("hello");
s.push_str(", world!");
println!("{s}");
```

