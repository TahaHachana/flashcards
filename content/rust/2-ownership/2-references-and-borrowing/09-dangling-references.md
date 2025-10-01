## Dangling References

Does Rust allow dangling references?

---

No. The compiler prevents them by enforcing lifetimes.
You cannot return a reference to a value that goes out of scope.

```rust
fn dangle() -> &String { // ❌ error
    let s = String::from("hello");
    &s
}
```

