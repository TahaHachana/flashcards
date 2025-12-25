## Integration Test File Structure

How do you structure a basic integration test file?

---

```rust
// tests/integration_test.rs

// Import your library as external user
use my_project;

#[test]
fn test_public_api() {
    let result = my_project::public_function(5);
    assert_eq!(result, 10);
}

#[test]
fn test_module_integration() {
    let obj = my_project::MyStruct::new(42);
    assert_eq!(obj.get_value(), 42);
}
```

Key points:
- No `#[cfg(test)]` module needed
- Import crate by name from Cargo.toml
- Only test public APIs
- Use `#[test]` attribute on functions

