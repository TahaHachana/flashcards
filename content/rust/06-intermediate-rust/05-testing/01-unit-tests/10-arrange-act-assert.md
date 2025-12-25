## Arrange-Act-Assert Pattern

What is the Arrange-Act-Assert (AAA) pattern for structuring tests?

---

AAA structures tests in three clear phases:

1. **Arrange**: Set up test data and preconditions
2. **Act**: Perform the operation being tested
3. **Assert**: Verify the result

Example:
```rust
#[test]
fn test_user_creation() {
    // Arrange: Set up test data
    let name = "Alice";
    let age = 30;
    
    // Act: Perform operation
    let user = User::new(name, age);
    
    // Assert: Verify result
    assert_eq!(user.name(), name);
    assert_eq!(user.age(), age);
}
```

This pattern makes tests readable and maintainable.

