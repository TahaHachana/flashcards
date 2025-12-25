## Testing Error Propagation Pattern

How do you test error handling in integration tests?

---

Test that errors propagate correctly and are usable:

```rust
use my_project::{parse_config, ConfigError};

#[test]
fn test_missing_field_error() {
    let result = parse_config("incomplete.toml");
    
    assert!(result.is_err());
    match result {
        Err(ConfigError::MissingField(field)) => {
            assert_eq!(field, "database_url");
        }
        _ => panic!("Expected MissingField error"),
    }
}

#[test]
fn test_invalid_format_error() {
    let result = parse_config("invalid.toml");
    assert!(matches!(result, Err(ConfigError::InvalidFormat(_))));
}
```

This verifies:
- Error types are public and usable
- Error variants carry correct information
- Error messages are helpful

