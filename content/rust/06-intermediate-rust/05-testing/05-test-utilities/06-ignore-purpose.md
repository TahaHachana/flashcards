## #[ignore] Attribute Purpose

What does `#[ignore]` do and when should you use it?

---

`#[ignore]` skips tests during normal `cargo test`:

```rust
#[test]
fn fast_test() {
    assert_eq!(2 + 2, 4);  // Always runs
}

#[test]
#[ignore]
fn slow_test() {
    expensive_operation();  // Skipped by default
}
```

Running ignored tests:
```bash
cargo test               # Skips ignored
cargo test -- --ignored  # Only ignored
cargo test -- --include-ignored  # All
```

Use for:
- Slow tests (minutes+)
- External dependencies (network, database)
- Platform-specific tests
- Temporarily broken tests (with TODO)

Output:
```
test fast_test ... ok
test slow_test ... ignored

test result: ok. 1 passed; 0 failed; 1 ignored
```

Keeps default test runs fast while preserving comprehensive tests.

