## When to Use Integration Tests

When should you write integration tests versus relying solely on unit tests?

---

Write integration tests when:

1. **Testing module interactions**:
```rust
#[test]
fn parser_validator_processor_work_together() {
    let parsed = parse(input).unwrap();
    let validated = validate(parsed).unwrap();
    let result = process(validated).unwrap();
    assert_eq!(result.status, Expected);
}
```

2. **Verifying public API usability**:
- Can users accomplish their goals?
- Is the API ergonomic?

3. **Testing complete workflows**:
- User registration flow
- Data processing pipeline
- Request/response cycle

4. **Catching integration bugs**:
- Issues only visible when components combine
- Configuration problems
- Resource management

Don't need integration tests for:
- Individual pure functions (use unit tests)
- Internal implementation details
- Already well-tested by unit tests

Balance: Many unit tests + strategic integration tests.

