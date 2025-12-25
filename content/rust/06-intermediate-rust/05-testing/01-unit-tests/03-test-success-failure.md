## Test Success vs Failure Mechanism

How does Rust determine if a test passes or fails?

---

A test passes if the function completes without panicking.
A test fails if the function panics.

Any panic source causes failure:
- `assert!()` macro
- `unwrap()` on `None` or `Err`
- `expect()` on `None` or `Err`
- `panic!()` macro
- Index out of bounds

Example:
```rust
#[test]
fn passes() {
    assert_eq!(2, 2); // No panic → pass
}

#[test]
fn fails() {
    assert_eq!(2, 3); // Panics → fail
}
```

