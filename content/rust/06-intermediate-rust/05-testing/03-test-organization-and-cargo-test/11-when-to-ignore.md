## When to Ignore Tests

What are good use cases for marking tests with `#[ignore]`?

---

Use `#[ignore]` for:

1. **Slow tests**:
```rust
#[test]
#[ignore]
fn full_system_integration() {
    // Takes 5+ minutes
}
```

2. **External dependencies**:
```rust
#[test]
#[ignore]
fn test_database_connection() {
    // Requires running PostgreSQL
}

#[test]
#[ignore]
fn test_api_call() {
    // Requires internet and API key
}
```

3. **Platform-specific**:
```rust
#[test]
#[ignore]
#[cfg(target_os = "linux")]
fn linux_only_test() { }
```

4. **Temporarily broken** (with comment):
```rust
#[test]
#[ignore]  // TODO: Fix bug #123
fn currently_broken() { }
```

Benefits: Keep default `cargo test` fast while preserving slow/special tests.

