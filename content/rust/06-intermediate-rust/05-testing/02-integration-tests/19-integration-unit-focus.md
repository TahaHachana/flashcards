## Integration vs Unit Test Focus

What should integration tests focus on versus unit tests?

---

Unit tests: Test individual components
```rust
#[cfg(test)]
mod tests {
    #[test]
    fn test_parse() {
        assert!(parse("input").is_ok());
    }
    
    #[test]
    fn test_validate() {
        assert!(validate(data).is_ok());
    }
}
```

Integration tests: Test workflows and integration
```rust
// tests/workflow.rs
#[test]
fn test_parse_and_validate_workflow() {
    let parsed = my_project::parse("input").unwrap();
    let validated = my_project::validate(parsed).unwrap();
    assert_eq!(validated.status, Status::Valid);
}
```

Write many fast unit tests, fewer comprehensive integration tests.

