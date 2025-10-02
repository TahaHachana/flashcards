## Match Ergonomics

What are match ergonomics in Rust?

---

Rust automatically dereferences or borrows values when matching.
Explicit `ref` or `ref mut` can still be used:

```rust
let s = Some(String::from("hi"));

match &s {
    Some(v) => println!("len = {}", v.len()), // borrowed, not moved
    None => {}
}
```

