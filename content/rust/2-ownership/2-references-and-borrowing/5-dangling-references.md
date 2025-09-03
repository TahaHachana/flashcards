# Dangling References

What is a dangling reference, and why does Rust forbid it?

---

A dangling reference points to memory that has been deallocated. Rust’s borrow checker prevents returning references to local data that goes out of scope, avoiding invalid memory access.

```rust
// ERROR: returns &String to local `s`
fn dangle() -> &String {
    let s = String::from("hello");
    &s
}
// `s` goes out of scope here, so &s is a dangling reference
```