## Release Mode Testing

How do you run tests in release mode and why might you need to?

---

Run tests with optimizations:

```bash
cargo test --release
```

Why use release mode:

1. **Performance testing**:
```rust
#[test]
fn test_algorithm_speed() {
    let start = Instant::now();
    expensive_algorithm();
    assert!(start.elapsed() < Duration::from_secs(1));
}
```

2. **Different behavior** (e.g., overflow):
```rust
#[test]
fn test_overflow() {
    let x: u8 = 255;
    let y = x + 1;  // Debug: panics, Release: wraps to 0
}
```

3. **Real-world conditions**:
- Tests behavior as users will experience it
- Catches optimization-related bugs

Note: Debug mode has extra checks (overflow, assertions) that release mode doesn't.

