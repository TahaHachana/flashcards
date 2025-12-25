## Custom Environment Variables in Tests

How can you use custom environment variables in tests?

---

Set variables in test code or shell:

In test code:
```rust
#[test]
fn test_with_env() {
    std::env::set_var("TEST_MODE", "true");
    std::env::set_var("API_KEY", "test_key");
    
    // Test code that reads these variables
    assert_eq!(std::env::var("TEST_MODE").unwrap(), "true");
}
```

From shell:
```bash
API_KEY=test_key cargo test

# Multiple variables
TEST_MODE=true API_KEY=test cargo test
```

Check environment in code:
```rust
#[test]
fn test_config() {
    if std::env::var("CI").is_ok() {
        // Running in CI environment
        use_ci_specific_config();
    } else {
        // Local development
        use_local_config();
    }
}
```

Common pattern: Use env vars to control test behavior without changing code.

