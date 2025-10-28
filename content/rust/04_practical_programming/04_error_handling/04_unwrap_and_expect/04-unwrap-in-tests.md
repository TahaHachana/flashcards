## Unwrap In Tests

Why is it acceptable to use `unwrap()` and `expect()` liberally in tests?

---

Tests are the ideal place for `unwrap()` and `expect()`:

```rust
#[test]
fn test_parsing() {
    let result = parse_input("42").unwrap();
    assert_eq!(result, 42);
    
    let config = load_config("test.toml")
        .expect("Test config must be valid");
    assert_eq!(config.port, 8080);
}
```

**Why it's okay:**
- Test failures need to be obvious - panics make them clear
- Panics in tests are caught and reported by the test framework
- You want tests to stop immediately on unexpected errors
- No need for error propagation in test code
- The panic message becomes part of the test failure report

