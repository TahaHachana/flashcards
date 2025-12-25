## One Assertion Per Test Guideline

When should you use one assertion per test vs multiple assertions?

---

One assertion per test (preferred):
```rust
#[test]
fn test_addition() {
    assert_eq!(add(2, 2), 4);
}

#[test]
fn test_multiplication() {
    assert_eq!(multiply(3, 3), 9);
}
```

Benefits:
- Each test has focused purpose
- Failures point to specific scenarios
- Tests run in parallel
- Can run individual tests

Multiple assertions (acceptable exception):
```rust
#[test]
fn test_user_initialization() {
    let user = User::new("Alice", 30);
    assert_eq!(user.name(), "Alice");  // Related
    assert_eq!(user.age(), 30);        // Related
    assert!(user.is_active());         // Related
}
```

Use multiple assertions only when testing related properties of the same object.

