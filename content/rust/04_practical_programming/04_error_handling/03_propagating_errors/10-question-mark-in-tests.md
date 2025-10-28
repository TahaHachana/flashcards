## Question Mark In Tests

How and why do you use `?` in test functions?

---

Tests can return `Result` to enable using `?` for cleaner error handling:

```rust
#[test]
fn test_parsing() -> Result<(), Box<dyn std::error::Error>> {
    let config = parse_config("test.txt")?;
    assert_eq!(config.port, 8080);
    Ok(())
}
```

Benefits:
- Cleaner than unwrap/expect in complex setup
- Test failures include the error message automatically
- Enables using `?` with file I/O, parsing, etc. in tests

If the test returns `Err`, the test framework marks it as failed.

