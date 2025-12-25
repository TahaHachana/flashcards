## Fast Tests Best Practice

How do you keep your test suite fast while maintaining comprehensive coverage?

---

Strategies:

1. **Mark slow tests as ignored**:
```rust
#[test]
fn fast_test() {
    // Runs every time (milliseconds)
}

#[test]
#[ignore]
fn slow_integration_test() {
    // Run manually (minutes)
}
```

2. **Run unit tests frequently, integration rarely**:
```bash
# During development (fast)
cargo test --lib

# Before commit (comprehensive)
cargo test -- --include-ignored
```

3. **Mock external dependencies**:
```rust
// ❌ Slow: actual API call
#[test]
fn test_api() {
    let response = api_call();
}

// ✅ Fast: mock response
#[test]
fn test_api() {
    let response = MockResponse::new();
}
```

4. **Minimize I/O**:
- Use in-memory databases
- Avoid file system
- Mock network calls

Goal: Keep default `cargo test` under 1-2 seconds.

