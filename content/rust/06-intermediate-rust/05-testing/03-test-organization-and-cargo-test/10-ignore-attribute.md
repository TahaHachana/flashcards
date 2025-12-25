## The #[ignore] Attribute

What does `#[ignore]` do and how do you run ignored tests?

---

`#[ignore]` marks tests to skip by default:

```rust
#[test]
#[ignore]
fn expensive_test() {
    // Takes 10 minutes
}

#[test]
fn fast_test() {
    // Runs normally
}
```

Running tests:
```bash
# Default: skips ignored tests
cargo test
# Output: 1 passed; 0 failed; 1 ignored

# Run ONLY ignored tests
cargo test -- --ignored

# Run ALL tests (including ignored)
cargo test -- --include-ignored
```

Use for:
- Slow tests
- Tests requiring external resources (network, database)
- Platform-specific tests
- Temporarily broken tests

