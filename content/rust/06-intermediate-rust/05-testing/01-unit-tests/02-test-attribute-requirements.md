## The #[test] Attribute Requirements

What are the three requirements for a function marked with `#[test]` in Rust?

---

Test functions must:
1. Take no parameters (cannot have any arguments)
2. Return `()` (unit type) or `Result<(), E>`
3. Not be called from regular code (only run via `cargo test`)

Example:
```rust
#[test]
fn valid_test() {
    assert_eq!(2 + 2, 4);
}
```

Tests are only compiled and executed when running `cargo test`.

