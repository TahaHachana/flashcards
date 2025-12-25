## Error Message Best Practices

How should you write helpful error messages in test assertions?

---

Provide context and actual values:

Bad:
```rust
#[test]
fn test_age() {
    let user = create_user("Alice", 15);
    assert!(user.age() >= 18);  // Unhelpful: "assertion failed"
}
```

Good:
```rust
#[test]
fn test_age() {
    let user = create_user("Alice", 15);
    assert!(
        user.age() >= 18,
        "User {} must be 18+, but age is {}",
        user.name(),
        user.age()
    );
}
```

Helper with good messages:
```rust
fn assert_valid_age(user: &User) {
    assert!(
        user.age() >= 18 && user.age() <= 150,
        "User '{}' has invalid age: {} (must be 18-150)",
        user.name(),
        user.age()
    );
}
```

Good error messages:
- Explain what was expected
- Show actual values
- Provide context
- Help identify the problem quickly

Failed test output should be immediately actionable.

