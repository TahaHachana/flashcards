## Helpful Failure Messages Practice

How do you write helpful custom failure messages in tests?

---

Include context about what was being tested and why it matters:

Less helpful:
```rust
#[test]
fn test_validation() {
    assert!(validate_email("invalid"));
    // Just says: assertion failed
}
```

More helpful:
```rust
#[test]
fn test_validation() {
    let email = "invalid@";
    assert!(
        validate_email(email),
        "Email '{}' should be valid but was rejected",
        email
    );
}

#[test]
fn test_age_requirement() {
    let user_age = 15;
    assert!(
        user_age >= 18,
        "Expected user age {} to meet minimum requirement of 18",
        user_age
    );
}
```

Good messages include:
- What value was being tested
- What was expected
- Why the test matters

