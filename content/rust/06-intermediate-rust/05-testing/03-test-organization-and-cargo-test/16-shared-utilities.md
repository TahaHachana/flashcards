## Shared Test Utilities

How do you create and use shared helper functions in test modules?

---

Create helper functions in the test module:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    // Shared setup (not a test - no #[test])
    fn setup() -> TestContext {
        TestContext {
            database: TestDatabase::new(),
            config: TestConfig::default(),
        }
    }
    
    // Shared assertions
    fn assert_valid_user(user: &User) {
        assert!(user.age() > 0);
        assert!(!user.name().is_empty());
    }
    
    #[test]
    fn test_create_user() {
        let ctx = setup();
        let user = ctx.create_user("Alice", 30);
        assert_valid_user(&user);
    }
    
    #[test]
    fn test_update_user() {
        let ctx = setup();
        let mut user = ctx.create_user("Bob", 25);
        user.update_age(26);
        assert_valid_user(&user);
    }
}
```

Benefits: Reduce duplication, consistent setup, reusable assertions.

