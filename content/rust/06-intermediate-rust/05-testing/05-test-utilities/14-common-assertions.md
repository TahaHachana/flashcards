## Common Assertions Helper

How do you create reusable assertion helpers for tests?

---

Create assertion functions in test helpers:

```rust
#[cfg(test)]
mod test_helpers {
    use super::*;
    
    pub fn assert_user_valid(user: &User) {
        assert!(!user.name().is_empty(), "Name must not be empty");
        assert!(user.age() > 0, "Age must be positive");
        assert!(user.email().contains('@'), "Email must be valid");
    }
    
    pub fn assert_response_ok(response: &Response) {
        assert_eq!(response.status(), 200);
        assert!(!response.body().is_empty());
    }
    
    pub fn assert_in_range(value: i32, min: i32, max: i32) {
        assert!(
            value >= min && value <= max,
            "Expected {} in range [{}, {}]", value, min, max
        );
    }
}

#[test]
fn test_user() {
    let user = create_user("Alice", 30, "alice@example.com");
    test_helpers::assert_user_valid(&user);
}
```

Benefits: Consistent checks, better error messages, DRY principle.

