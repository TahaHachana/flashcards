## Test Helper Functions

How do you create and use helper functions in test modules?

---

Helper functions don't need `#[test]` and can be called by multiple tests:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    // Helper function (no #[test])
    fn create_test_user() -> User {
        User::new("TestUser", 25)
    }
    
    fn setup_environment() -> TestContext {
        TestContext {
            database: TestDatabase::new(),
            config: TestConfig::default(),
        }
    }
    
    #[test]
    fn test_operations() {
        let user = create_test_user();  // Use helper
        assert!(user.is_valid());
    }
}
```

Benefits: Reduce duplication, centralize test setup logic.

